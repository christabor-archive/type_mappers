"""Tests."""

import pytest

import type_mappers


def test_get_all_context_fields():
    """Test using the getter function returns the right fields."""
    for ctx, mappings in type_mappers.all_maps.items():
        for fieldname, mapping in mappings.items():
            if mapping is not None:
                assert type_mappers.get_context_field(
                    fieldname, ctx) == mapping


def test_get_not_implemented_fields():
    """Test using the getter function throws errors."""
    for ctx, mappings in type_mappers.all_maps.items():
        for fieldname, mapping in mappings.items():
            if mapping is None:
                with pytest.raises(NotImplementedError):
                    type_mappers.get_context_field(fieldname, ctx) == mapping


def test_get_not_implemented_fields_with_str_fallback():
    """Get invalid field w/ fallback."""
    for ctx, mappings in type_mappers.all_maps.items():
        for fieldname, mapping in mappings.items():
            if mapping is None:
                assert type_mappers.get_context_field(
                    fieldname, ctx, fallback='str')
