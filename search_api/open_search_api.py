# coding=utf-8
import time
import json
import requests


def search(cql_keywords=("=", ""),
           cql_resultSetId=("=", ""),
           dc_creator=("=", ""),
           dc_description=("=", ""),
           dc_identifier=("=", ""),
           dc_publisher=("=", ""),
           dc_subject=("=", ""),
           dc_title=("=", ""),
           dcterms_isPartOf=("=", ""),
           medline_chemical=("=", ""),
           medline_mesh=("=", ""),
           medline_pmid=("=", ""),
           palgraveconnect_affiliation=("=", ""),
           pam_status=("=", ""),
           prism_aggregationType=("=", ""),
           prism_channel=("=", ""),
           prism_copyright=("=", ""),
           prism_coverDate=("=", ""),
           prism_creationDate=("=", ""),
           prism_doi=("=", ""),
           prism_eIssn=("=", ""),
           prism_endingPage=("=", ""),
           prism_genre=("=", ""),
           prism_isbn=("=", ""),
           prism_issn=("=", ""),
           prism_number=("=", ""),
           prism_productCode=("=", ""),
           prism_publicationDate=("=", ""),
           prism_publicationName=("=", ""),
           prism_section=("=", ""),
           prism_startingPage=("=", ""),
           prism_subsection1=("=", ""),
           prism_url=("=", ""),
           prism_volume=("=", ""),
           maximum_records=25,
           start_record=1
           ):
    """execute search
    (see https://www.nature.com/opensearch/request)

    Args:
        cql_keywords: cql.keywords index specified with tuple (RELATION, "TERM")
        cql_resultSetId: cql.resultSetId index specified with tuple (RELATION, "TERM")
        dc_creator: dc.creator index specified with tuple (RELATION, "TERM")
        dc_description: dc.description index specified with tuple (RELATION, "TERM")
        dc_identifier: dc.identifier index specified with tuple (RELATION, "TERM")
        dc_publisher: dc.publisher index specified with tuple (RELATION, "TERM")
        dc_subject: dc.subject index specified with tuple (RELATION, "TERM")
        dc_title: dc.title index specified with tuple (RELATION, "TERM")
        dcterms_isPartOf: dcterms.isPartOf index specified with tuple (RELATION, "TERM")
        medline_chemical: medline.chemical index specified with tuple (RELATION, "TERM")
        medline_mesh: medline.mesh index specified with tuple (RELATION, "TERM")
        medline_pmid: medline.pmid index specified with tuple (RELATION, "TERM")
        palgraveconnect_affiliation: palgraveconnect.affiliation index specified with tuple (RELATION, "TERM")
        pam_status: pam.status index specified with tuple (RELATION, "TERM")
        prism_aggregationType: prism.aggregationType index specified with tuple (RELATION, "TERM")
        prism_channel: prism.channel index specified with tuple (RELATION, "TERM")
        prism_copyright: prism.copyright index specified with tuple (RELATION, "TERM")
        prism_coverDate: prism.coverDate index specified with tuple (RELATION, "TERM")
        prism_creationDate: prism.creationDate index specified with tuple (RELATION, "TERM")
        prism_doi: prism.doi index specified with tuple (RELATION, "TERM")
        prism_eIssn: prism.eIssn index specified with tuple (RELATION, "TERM")
        prism_endingPage: prism.endingPage index specified with tuple (RELATION, "TERM")
        prism_genre: prism.genre index specified with tuple (RELATION, "TERM")
        prism_isbn: prism.isbn index specified with tuple (RELATION, "TERM")
        prism_issn: prism.issn index specified with tuple (RELATION, "TERM")
        prism_number: prism.number index specified with tuple (RELATION, "TERM")
        prism_productCode: prism.productCode index specified with tuple (RELATION, "TERM")
        prism_publicationDate: prism.publicationDate index specified with tuple (RELATION, "TERM")
        prism_publicationName: prism.publicationName index specified with tuple (RELATION, "TERM")
        prism_section: prism.section index specified with tuple (RELATION, "TERM")
        prism_startingPage: prism.startingPage index specified with tuple (RELATION, "TERM")
        prism_subsection1: prism.subsection1 index specified with tuple (RELATION, "TERM")
        prism_url: prism.url index specified with tuple (RELATION, "TERM")
        prism_volume: prism.volume index specified with tuple (RELATION, "TERM")
        maximum_records: maximum.records index specified with tuple (RELATION, "TERM")
        start_record: start.record index specified with tuple (RELATION, "TERM")

    Returns:
        search result (json object)

    Note:
        all indexes are joined with "AND"

    """

    indexes_dictionary = {"cql.keywords": cql_keywords,
                          "cql.resultSetId": cql_resultSetId,
                          "dc.creator": dc_creator,
                          "dc.description": dc_description,
                          "dc.identifier": dc_identifier,
                          "dc.publisher": dc_publisher,
                          "dc.subject": dc_subject,
                          "dc.title": dc_title,
                          "dcterms.isPartOf": dcterms_isPartOf,
                          "medline.chemical": medline_chemical,
                          "medline.mesh": medline_mesh,
                          "medline.pmid": medline_pmid,
                          "palgraveconnect.affiliation": palgraveconnect_affiliation,
                          "pam.status": pam_status,
                          "prism.aggregationType": prism_aggregationType,
                          "prism.channel": prism_channel,
                          "prism.copyright": prism_copyright,
                          "prism.coverDate": prism_coverDate,
                          "prism.creationDate": prism_creationDate,
                          "prism.doi": prism_doi,
                          "prism.eIssn": prism_eIssn,
                          "prism.endingPage": prism_endingPage,
                          "prism.genre": prism_genre,
                          "prism.isbn": prism_isbn,
                          "prism.issn": prism_issn,
                          "prism.number": prism_number,
                          "prism.productCode": prism_productCode,
                          "prism.publicationDate": prism_publicationDate,
                          "prism.publicationName": prism_publicationName,
                          "prism.section": prism_section,
                          "prism.startingPage": prism_startingPage,
                          "prism.subsection1": prism_subsection1,
                          "prism.url": prism_url,
                          "prism.volume": prism_volume}

    query = "+AND+".join([make_each_query(item[0], item[1][0], item[1][1]) for item in indexes_dictionary.items()
                          if item[1][1] != ""])
    maximum_records = maximum_records
    start_record = start_record

    url = "https://www.nature.com/opensearch/request?" + \
          "query={0}&httpAccept=application%2Fjson&maximumRecords={1}&startRecord={2}".format(
              query, maximum_records, start_record)

    return json.loads(requests.get(url).text)


def make_each_query(index, relation, term):
    """make query for each index
    
    Args:
        index: descriptor
        relation: relation in ["=", "==", "<>", "adj", "all", "any"]
        term: argument string

    Returns:
        descriptor + relation + "arguments"
    """
    relation_dictionary = {"=": "%3D", "==": "%3D%3D", "<>": "<>", "adj": "adj", "all": "all", "any": "any"}

    return "+".join([index, relation_dictionary[relation]]) + "+\"" + "+".join(term.split(" ")) + "\""
