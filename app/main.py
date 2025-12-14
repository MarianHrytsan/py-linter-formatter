def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "line": data_error["line_number"],
                "column": data_error["column_number"],
                "message": data_error["text"],
                "name": data_error["code"],
                "source": "flake8",
            }
            for data_error in errors
            if data_error["filename"] == file_path
        ],
        "path": file_path,
        "status": "failed" if any(errors) else "passed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": err["line_number"],
                    "column": err["column_number"],
                    "message": err["text"],
                    "name": err["code"],
                    "source": "flake8",
                }
                for err in data_error
                if any(data_error)
            ],
            "path": road_to_file,
            "status": "failed" if any(data_error) else "passed",
        }
        for road_to_file, data_error in linter_report.items()
    ]
