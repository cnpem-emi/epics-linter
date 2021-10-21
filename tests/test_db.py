def test_valid_with_quotes(linter, capfd):
    linter.lint(
        """record(ai, "foobar") {
    field(DESC, "Description")
    field(DTYP, "stream")
    field(EGU, "$(EGU)")
    }"""
    )

    out, _ = capfd.readouterr()
    assert out == ""


def test_valid_with_words(linter, capfd):
    linter.lint(
        """record(ai, foobar) {
    field(DESC, Description)
    field(DTYP, stream)
    field(EGU, "$(EGU)")
    }"""
    )

    out, _ = capfd.readouterr()
    assert out == ""


def test_no_closing_bracket(linter, capfd):
    linter.lint(
        """record(ai, foobar) {
    field(DESC, Description)
    field(DTYP, stream)
    field(EGU, "$(EGU)")"""
    )

    out, _ = capfd.readouterr()
    assert out == "'}' expected at 4:24\n"


def test_no_opening_bracket(linter, capfd):
    linter.lint(
        """record(ai, foobar)
    field(DESC, Description)
    field(DTYP, stream)
    field(EGU, "$(EGU)")
    }"""
    )

    out, _ = capfd.readouterr()
    assert out == "'{' expected at 2:5\n"


def test_too_many_arguments(linter, capfd):
    linter.lint(
        """record(ai, "foobar") {
    field(DESC, "Description", a)
    }"""
    )

    out, _ = capfd.readouterr()
    assert out == "Too many arguments at 2:32\n"


def test_too_many_arguments_head(linter, capfd):
    linter.lint(
        """record(ai, "foobar", foo) {
    field(DESC, "Description")
    }"""
    )

    out, _ = capfd.readouterr()
    assert out == "Too many arguments at 1:22\n"


def test_too_many_arguments_both(linter, capfd):
    linter.lint(
        """record(ai, "foobar", foo) {
    field(DESC, "Description", "foo")
    }"""
    )

    out, _ = capfd.readouterr()
    assert out == "Too many arguments at 1:22\nToo many arguments at 2:32\n"


def test_no_close_quote(linter, capfd):
    linter.lint(
        """record(ai, "foobar", foo) {
    field(DESC, "Description", "foo")
    }"""
    )

    out, _ = capfd.readouterr()
    assert out == "Too many arguments at 1:22\nToo many arguments at 2:32\n"


def test_name_too_long(linter, capfd):
    linter.lint(
        """record(ai, {}) {{
    field(DESC, "Description")
    }}""".format(
            "a" * 62
        )
    )

    out, _ = capfd.readouterr()
    assert out == "Record name too long (maximum of 60) at 1:12 to 1:74\n"


def test_desc_too_long(linter, capfd):
    linter.lint(
        """record(ai, "foobar") {{
    field(DESC, {})
    }}""".format(
            "a" * 45
        )
    )

    out, _ = capfd.readouterr()
    assert out == "Record description too long (maximum of 40) at 2:17 to 2:62\n"
