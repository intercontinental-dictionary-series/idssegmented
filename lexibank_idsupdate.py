import pathlib
import regex as re
import attr
# from clldutils.misc import slug
from pylexibank import progressbar as pb
from pylexibank import Language
from pylexibank import FormSpec
import pycldf
from idspy import IDSDataset
from lingpy import Wordlist
from clldutils.misc import slug
from unidecode import unidecode
import re



class Dataset(IDSDataset):
    dir = pathlib.Path(__file__).parent
    id = "idsupdate"
    form_spec = FormSpec(
            replacements=[
                ("1", "¹"),
                ("2", "²"),
                ("3", "³"),
                ("4", "⁴"),
                ("5", "⁵"),
                ("6", "⁶"),
                ("7", "⁷"),
                ("8", "⁸"),
                ("9", "⁹"),
                ("0", "⁰"),
                ("#", ""),
                 (" ", "_"),
                ], 
            separators="~;,/", missing_data=["∅"], first_form_only=True)

    def cmd_download(self, args):
        ids_data = pycldf.Dataset.from_metadata(
                self.raw_dir.joinpath('ids', 'cldf', 'cldf-metadata.json')
                )
        ids = set([row["IDS_ID"] for row in self.languages])

        bex = re.compile(r"\[(.+?)\]")

        def test_borrowed(word, value):
            if '[' not in value: return ""
            # Need to be sure it is this form.
            # Test to see if loan substring of value in form.
            # Use regex to get all borrowed substrings from value.
            # Test for whether any of borrowed substrings in form.
            loans = bex.findall(value)
            for loan in loans:
                if loan in word: return "1"
            # Not this form.
            return ""
        
        transc = set()
        with open(self.raw_dir.joinpath("ids-data.tsv").as_posix(), "w") as f:
            f.write("\t".join([
                "ID", "FORM_ID", "DOCULECT", "DOCULECT_ID", "CONCEPT", "CONCEPT_ID",
                "VALUE", "FORM", "TRANSCRIPTIONS", "ALTVALS", "BORROWING"])+"\n") 
            for i, form in pb(enumerate(ids_data.objects("FormTable")), desc="adding forms"):
                for t in form.data["Transcriptions"]:
                    transc.add(t)
                f.write("\t".join([
                    str(i+1),
                    form.id,
                    form.language.name,
                    form.language.id,
                    form.parameter.name,
                    form.parameter.id,
                    form.data["Value"],
                    form.data["Form"],
                    ";".join(form.data["Transcriptions"]),
                    "//".join(form.data["AlternativeValues"]),
                    test_borrowed(
                        word=form.data["Form"], 
                        value=form.data["Value"]
                        )
                    ])+"\n")

        for t in transc:
            args.log.info("Transcription: "+t)

    def cmd_makecldf(self, args):
        # add bib
        args.writer.add_sources()
        args.log.info("added sources")

        ids_data = pycldf.Dataset.from_metadata(
                self.raw_dir.joinpath('ids', 'cldf', 'cldf-metadata.json')
                )

        for concept in ids_data.objects('ParameterTable'):
            args.writer.add_concept(
                    **concept.data)

        def add_language_(lang):
            data = {k: lang.data[k] for k in ["ID", "Name", "Glottocode", 
                                             "ISO639P3code", "Latitude",
                                             "Longitude"
                                             ]}
            data["ID"] = slug(data["Name"])
            args.writer.add_language(**data)
                
        for language in ids_data.objects("LanguageTable"):
            add_language_(language)
        args.log.info("added languages and concepts")
        
        def add_form_(wl, idx):
            if wl[idx, "transcriptions"] == "CyrillTrans;Phonemic":
                form, alt = wl[idx, "altvals"], wl[idx, "form"]
            elif wl[idx, "transcriptions"] == "LatinTrans;Phonemic":
                form, alt = wl[idx, "altvals"], wl[idx, "form"]
            elif wl[idx, "transcriptions"] == "Standard;Phonemic":
                form, alt = wl[idx, "altvals"], wl[idx, "form"]
            else:
                form, alt = wl[idx, "form"], wl[idx, "altvals"]
            try:
                form = re.split(";|,", form)[0] 
            except IndexError:
                form = ""
            if form:
                form = self.form_spec.clean(form).replace(" ", "_")
                if wl[idx, "transcriptions"] == "CyrillTrans":
                    form = unidecode(form)
                args.writer.add_form(
                    ID=wl[idx, "form_id"],
                    Language_ID=slug(wl[idx, "doculect"]),
                    Parameter_ID=wl[idx, "concept_id"],
                    Form=form,
                    Value=wl[idx, "value"],
                    Transcriptions=wl[idx, "transcriptions"],
                    AlternativeValues=alt,
                    Loan=True if wl[idx, "borrowing"] else False)
            else:
                args.log.info("excluding: "+wl[idx, "value"])
                
        wl = Wordlist(self.raw_dir.joinpath("ids-data.tsv").as_posix())
        for idx in pb(wl, desc="adding forms"):
            add_form_(wl, idx)
