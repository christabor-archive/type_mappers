"""Tests."""

import type_mappers


def test_all_context_fields_match():
    """Ensure all ctxs have the same number of keys for consistency."""
    counts = dict()
    for ctx, mappings in type_mappers.all_maps.items():
        counts[ctx] = len(mappings)

    first_ctx_count = list(counts.items())[0][1]

    for ctx, mappings in type_mappers.all_maps.items():
        err_msg = '"{}" does not match the length of others: {}'.format(
            ctx, counts)
        assert len(type_mappers.all_maps[ctx]) == first_ctx_count, err_msg


def test_all_context_fields_in_order():
    """Ensure all ctxs have the same fields in the same order."""
    mappings = type_mappers.all_maps.values()
    counts = []
    for ctx, mappings in type_mappers.all_maps.items():
        counts.append([ctx, sorted(mappings)])

    for i, item in enumerate(counts):
        if i > 0:
            ctx, mappings = item
            fst, snd = counts[i], counts[i - 1]
            err_msg = '"{} ({})" does not match "{} ({})"'.format(
                fst[0], len(fst[1]), snd[0], len(snd[1])
            )
            assert fst[1] == snd[1], err_msg


def test_all_mappings_are_callable():
    """Test functions."""
    for ctx, mappings in type_mappers.all_maps.items():
        for name, mapping in mappings.items():
            if mapping is not None:
                assert hasattr(mapping, '__call__')
