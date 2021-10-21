class InvalidDeclaration:
    label = "Invalid declaration inside record when field() was expected"


class OpeningBraceExpected:
    label = "'{' expected"


class ClosingBraceExpected:
    label = "'}' expected"


class ClosingQuoteExpected:
    label = "'\"' expected"


class TooManyArguments:
    label = "Too many arguments"


class TooFewArguments:
    label = "Too few arguments"


DB_ERROR = {
    TooManyArguments: [
        'record(foo, "bar", foo)',
        'record(foo, "bar") {\n field(foo, "bar", bar)\n }',
        'record(foo, "bar") {\n field(foo, bar, bar)\n }',
        'record(foo, "bar") {\n field(foo, bar, "bar")\n }',
        'record(foo, "bar") {\n field(foo, "bar", "bar")\n }',
    ],
    ClosingQuoteExpected: [
        'record(foo, "bar) {\n field(DESC, "bar")\n}',
        'record(foo, "bar) {\n bar \n}',
        'record(foo, "bar") {\n field(DESC, "bar)\n}',
        'record(foo, "bar") {\n field(DESC, "bar")\n field(DESC, "bar)\n}',
    ],
    TooFewArguments: ["record(foo)", "record(foo,)"],
    InvalidDeclaration: [
        'record(ai, "foo) {\nfoo(bar, "bar")}',
        'record(foo, "bar") {\n bar }',
        'record(foo, "bar") {\n field(DESC, "bar")\n foo(EVNT, "aaa")\n}',
    ],
    OpeningBraceExpected: [
        'record(foo, "bar") \nfield(DESC, "bar")\n}',
        'record(foo, bar) \nfield(DESC, "bar")\n}',
    ],
    ClosingBraceExpected: [
        'record(foo, "bar") {\n field(DESC, "bar") \nrecord(foo, "bar")',
        'record(ai, "bar") {\n field(DESC, "bar") \nfield(DTYP, "stream") \nrecord(foo, "bar")',
        'record(ai, "a) {\n field(foo, bar)',
        'record(ai, "a") {\n field(foo, bar)',
        'record(foo, "bar") {\n field(DESC, "bar")\n field(EVNT, "aaa")}',
    ],
}

DESC_TOO_LONG = "Record description too long (maximum of 40)"
REC_TOO_LONG = "Record name too long (maximum of 60)"
