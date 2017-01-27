import pytest

import type_mappers


def test_all_context_fields_match():
    """Ensure all contexts have the same number of keys for consistency."""
    first_ctx_count = None
    for context, mapping in type_mappers.all_maps.items():
        if first_ctx_count is None:
            first_ctx_count = len(type_mappers.all_maps[context])

    for context, mapping in type_mappers.all_maps.items():
        assert len(type_mappers.all_maps[context]) == first_ctx_count
