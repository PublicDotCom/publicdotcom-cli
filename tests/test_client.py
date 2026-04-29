from publicdotcom_cli.client import compact_params


def test_compact_params_removes_empty_values_and_expands_lists() -> None:
    assert compact_params(
        {
            "typeFilter": ["EQUITY", "OPTION"],
            "empty": None,
            "alsoEmpty": [],
            "pageSize": 25,
        }
    ) == [
        ("typeFilter", "EQUITY"),
        ("typeFilter", "OPTION"),
        ("pageSize", 25),
    ]
