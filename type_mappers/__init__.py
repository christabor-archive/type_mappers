"""A spec and code to implement the spec.

The spec defines a generic mapper for types to other types,
which can be used for validation, code generation and more.

NOTE: The below imports are always wrapped in a try/catch block
to ensure that users can optionally use/install one or more without having
to install them all.
"""

from decimal import Decimal

from datetime import date
from datetime import datetime


try:
    # Py3 only.
    from enum import Enum
except ImportError:
    Enum = None

try:
    # Py3 uses unicode for str.
    unicode
except NameError:
    unicode = str

vanilla = {
    # Numbers
    'int': int,
    'integer': int,
    'decimal': Decimal,
    'float': float,
    'number': int,
    'num': int,
    'int32': int,
    'int64': int,
    'uint32': int,
    'uint64': int,
    'double': float,
    'long': float,

    # Strings
    'str': str,
    'string': str,
    'unicode': unicode,

    # Booleans
    'true': bool,
    'false': bool,
    'bool': bool,

    # Dates
    'time': datetime,
    'datetime': datetime,
    'date': date,

    # Binary
    'file': bytes,
    'blob': bytes,
    'binary': bytes,
    'bytes': bytes,

    # Password
    'password': str,

    # Multi-choice
    'enum': Enum,

    # Configs/serialized formats - TODO: how best to map these.
    'pickle': None,
    'pkl': None,
    'json': None,
    'yaml': None,

    # Data structures - list
    'list': list,
    'array': list,

    # Data structures - dictionary
    'dict': dict,
    'dictionary': dict,

    # Data structures - tuple
    'tuple': tuple,
}

try:
    import sqlalchemy
    sqlalchemy_mapper = {
        # Numbers
        'int': sqlalchemy.Integer,
        'integer': sqlalchemy.Integer,
        'decimal': sqlalchemy.Float,
        'float': sqlalchemy.Float,
        'number': sqlalchemy.Integer,
        'num': sqlalchemy.Integer,
        'int32': sqlalchemy.SmallInteger,
        'int64': sqlalchemy.BigInteger,
        'uint32': sqlalchemy.SmallInteger,
        'uint64': sqlalchemy.BigInteger,
        'double': sqlalchemy.Float,
        'long': sqlalchemy.BigInteger,

        # Strings
        'str': sqlalchemy.String,
        'string': sqlalchemy.String,
        'unicode': sqlalchemy.Unicode,

        # Booleans
        'true': sqlalchemy.Boolean,
        'false': sqlalchemy.Boolean,
        'bool': sqlalchemy.Boolean,

        # Dates
        'time': sqlalchemy.Time,
        'datetime': sqlalchemy.DateTime,
        'date': sqlalchemy.Date,

        # Binary
        'file': sqlalchemy.BLOB,
        'blob': sqlalchemy.BLOB,
        'binary': sqlalchemy.Binary,
        'bytes': sqlalchemy.Binary,

        # Password
        'password': sqlalchemy.String,

        # Multi-choice
        'enum': sqlalchemy.Enum,

        # Configs/serialized formats
        'pickle': sqlalchemy.PickleType,
        'pkl': sqlalchemy.PickleType,
        'json': sqlalchemy.types.JSON,
        'yaml': None,

        # Data structures - list
        'list': sqlalchemy.types.ARRAY,
        'array': sqlalchemy.types.ARRAY,

        # Data structures - dictionary
        'dict': None,
        'dictionary': None,

        # Data structures - tuple
        'tuple': None,
    }
except ImportError:
    sqlalchemy_mapper = {}


try:
    import factory.fuzzy
    factoryboy_mapper = {
        # Numbers
        'int': factory.fuzzy.FuzzyInteger,
        'integer': factory.fuzzy.FuzzyInteger,
        'decimal': factory.fuzzy.FuzzyDecimal,
        'float': factory.fuzzy.FuzzyFloat,
        'number': factory.fuzzy.FuzzyInteger,
        'num': factory.fuzzy.FuzzyInteger,
        'int32': factory.fuzzy.FuzzyInteger,
        'int64': factory.fuzzy.FuzzyInteger,
        'uint32': factory.fuzzy.FuzzyInteger,
        'uint64': factory.fuzzy.FuzzyInteger,
        'double': factory.fuzzy.FuzzyFloat,
        'long': factory.fuzzy.FuzzyFloat,

        # Strings
        'str': factory.fuzzy.FuzzyText,
        'string': factory.fuzzy.FuzzyText,
        'unicode': factory.fuzzy.FuzzyText,

        # Booleans
        'true': None,
        'false': None,
        'bool': None,

        # Dates
        'time': factory.fuzzy.FuzzyDateTime,
        'datetime': factory.fuzzy.FuzzyDateTime,
        'date': factory.fuzzy.FuzzyDate,

        # Binary
        'file': None,
        'blob': None,
        'binary': None,
        'bytes': None,

        # Password
        'password': str,

        # Multi-choice
        'enum': factory.fuzzy.FuzzyChoice,

        # Configs/serialized formats
        'pickle': None,
        'pkl': None,
        'json': None,
        'yaml': None,

        # Data structures - list
        'list': factory.fuzzy.FuzzyChoice,
        'array': factory.fuzzy.FuzzyChoice,

        # Data structures - dictionary
        'dict': None,
        'dictionary': None,

        # Data structures - tuple
        'tuple': None,
    }
except ImportError:
    factoryboy_mapper = {}


try:
    import wtforms
    wtform_mapper = {
        # Numbers
        'int': wtforms.IntegerField,
        'integer': wtforms.IntegerField,
        'decimal': wtforms.DecimalField,
        'float': wtforms.DecimalField,  # Not using floatfield atm
        'number': wtforms.IntegerField,
        'num': wtforms.IntegerField,
        'int32': wtforms.IntegerField,
        'int64': wtforms.IntegerField,
        'uint32': wtforms.IntegerField,
        'uint64': wtforms.DecimalField,
        'double': wtforms.IntegerField,
        'long': wtforms.IntegerField,

        # Strings
        'str': wtforms.TextField,
        'string': wtforms.TextField,
        'unicode': wtforms.TextField,

        # Booleans
        'true': wtforms.BooleanField,
        'false': wtforms.BooleanField,
        'bool': wtforms.BooleanField,

        # Dates
        'time': wtforms.DateTimeField,
        'datetime': wtforms.DateTimeField,
        'date': wtforms.DateField,

        # Binary
        'file': wtforms.FileField,
        'blob': wtforms.FileField,
        'binary': wtforms.FileField,
        'bytes': wtforms.FileField,

        # Password
        'password': wtforms.PasswordField,

        # Multi-choice
        'enum': wtforms.SelectField,

        # Configs/serialized formats
        'pickle': wtforms.TextAreaField,
        'pkl': wtforms.TextAreaField,
        'json': wtforms.TextAreaField,
        'yaml': wtforms.TextAreaField,

        # Data structures - list
        'list': wtforms.SelectMultipleField,
        'array': wtforms.SelectMultipleField,

        # Data structures - dictionary
        'dict': None,
        'dictionary': None,

        # Data structures - tuple
        'tuple': None,
    }
except ImportError:
    wtform_mapper = {}


all_maps = {
    'vanilla': vanilla,
    'wtforms': wtform_mapper,
    'sqlalchemy': sqlalchemy_mapper,
    'factoryboy': factoryboy_mapper,
}


def get_context_field(fieldtype, context, fallback=None):
    """Given a context and a field, return the matching type.

    Args:
        fieldtype: The field type.
        context: The mapping context
        fallback: The name of the fallback string to use (default: {None})

    Returns:
        The field.
        None or callable, depending on the outcome.

    Raises:
        NotImplementedError: If no type exists
        NotImplementedError: If no specified fallback exists
    """
    fieldtype = fieldtype.lower()
    no_type_error = ('Type: "{}" for "{}" '
                     'has not been implemented'.format(fieldtype, context))
    try:
        typ = all_maps[context][fieldtype]
        if typ is None:
            if fallback is None:
                raise NotImplementedError(no_type_error)
            typ = all_maps[context][fallback]
            if typ is None:
                raise NotImplementedError(no_type_error)
        return typ
    except KeyError:
        return None
