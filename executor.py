# coding=utf-8
import search_api.open_search_api as search_api


def main():
    search_result = search_api.search(cql_keywords=("=", "physics quantum"), dc_title=("=", "physics"),
                                      maximum_records=100)

    entry_list = search_result["feed"]["entry"]
    for entry in entry_list:
        print(entry["title"])


if __name__ == "__main__":
    main()
