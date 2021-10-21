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
        'record(foo, "bar") { field(foo, "bar", bar) }',
        'record(foo, "bar") { field(foo, "bar", "bar") }',
        'record(foo, "bar") { field(foo, "bar", bar) }',
    ],
    ClosingQuoteExpected: [
        'record(foo, "bar) { field(DESC, "bar")}',
        'record(foo, "bar) { bar }',
        'record(foo, "bar") { field(DESC, "bar)}',
        'record(foo, "bar") { field(DESC, "bar") field(DESC, "bar)}',
    ],
    TooFewArguments: ["record(foo)", "record(foo,)"],
    InvalidDeclaration: [
        'record(ai, "foo") {foo(bar, "bar")}',
        'record(foo, "bar") { bar }',
    ],
    OpeningBraceExpected: [
        'record(foo, "bar") field(DESC, "bar")}',
        'record(foo, bar) field(DESC, "bar")',
    ],
    ClosingBraceExpected: [
        'record(foo, "bar") { field(DESC, "bar") record(foo, "bar")',
        'record(ai, "bar") { field(DESC, "bar") field(DTYP, "stream") record(foo, "bar")',
        'record(ai, "a) { field(foo, bar)',
        'record(ai, "a") { field(foo, bar)',
    ],
}

DESC_TOO_LONG = "Record description too long (maximum of 40)"
REC_TOO_LONG = "Record name too long (maximum of 60)"
