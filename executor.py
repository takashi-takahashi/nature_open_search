# coding=utf-8
import search_api.open_search_api as search_api


def main():
    # for each index one can feed (RELATION, "TERM") tuple
    # search result is given with json format
    search_result = search_api.search(cql_keywords=("=", "physics quantum"), dc_title=("=", "physics"),
                                      maximum_records=100)

    # a sample code to show titles
    entry_list = search_result["feed"]["entry"]
    for entry in entry_list:
        print(entry["title"])


if __name__ == "__main__":
    main()
