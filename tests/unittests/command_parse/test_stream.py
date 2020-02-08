def test_xrange(judge_command):
    judge_command(
        "XRANGE somestream - +",
        {"command": "XRANGE", "key": "somestream", "stream_id": ["-", "+"]},
    )
    judge_command(
        "XRANGE somestream  1526985054069 1526985055069",
        {
            "command": "XRANGE",
            "key": "somestream",
            "stream_id": ["1526985054069", "1526985055069"],
        },
    )
    judge_command(
        "XRANGE somestream  1526985054069 1526985055069-10",
        {
            "command": "XRANGE",
            "key": "somestream",
            "stream_id": ["1526985054069", "1526985055069-10"],
        },
    )
    judge_command(
        "XRANGE somestream  1526985054069 1526985055069-10 count 10",
        {
            "command": "XRANGE",
            "key": "somestream",
            "stream_id": ["1526985054069", "1526985055069-10"],
            "count_const": "count",
            "count": "10",
        },
    )


def test_xgroup_create(judge_command):
    judge_command(
        "XGROUP CREATE mykey mygroup 123",
        {
            "command": "XGROUP",
            "stream_create": "CREATE",
            "key": "mykey",
            "group": "mygroup",
            "stream_id": "123",
        },
    )
    judge_command(
        "XGROUP CREATE mykey mygroup $",
        {
            "command": "XGROUP",
            "stream_create": "CREATE",
            "key": "mykey",
            "group": "mygroup",
            "stream_id": "$",
        },
    )
    # short of a parameter
    judge_command("XGROUP CREATE mykey mygroup", None)
    judge_command("XGROUP CREATE mykey", None)


def test_xgroup_setid(judge_command):
    judge_command(
        "XGROUP SETID mykey mygroup 123",
        {
            "command": "XGROUP",
            "stream_setid": "SETID",
            "key": "mykey",
            "group": "mygroup",
            "stream_id": "123",
        },
    )
    judge_command(
        "XGROUP SETID mykey mygroup $",
        {
            "command": "XGROUP",
            "stream_setid": "SETID",
            "key": "mykey",
            "group": "mygroup",
            "stream_id": "$",
        },
    )
    # two subcommand together shouldn't match
    judge_command("XGROUP CREATE mykey mygroup 123 SETID mykey mygroup $", None)


def test_xgroup_destroy(judge_command):
    judge_command(
        "XGROUP destroy mykey mygroup",
        {
            "command": "XGROUP",
            "stream_destroy": "destroy",
            "key": "mykey",
            "group": "mygroup",
        },
    )
    judge_command("XGROUP destroy mykey", None)
    judge_command("XGROUP DESTROY mykey mygroup $", None)


def test_xgroup_delconsumer(judge_command):
    judge_command(
        "XGROUP delconsumer mykey mygroup myconsumer",
        {
            "command": "XGROUP",
            "stream_delconsumer": "delconsumer",
            "key": "mykey",
            "group": "mygroup",
            "consumer": "myconsumer",
        },
    )
    judge_command(
        "XGROUP delconsumer mykey mygroup $",
        {
            "command": "XGROUP",
            "stream_delconsumer": "delconsumer",
            "key": "mykey",
            "group": "mygroup",
            "consumer": "$",
        },
    )
    judge_command("XGROUP delconsumer mykey mygroup", None)


def test_xgroup_stream(judge_command):
    judge_command(
        "XACK mystream group1 123123",
        {
            "command": "XACK",
            "key": "mystream",
            "group": "group1",
            "stream_id": "123123",
        },
    )
    judge_command(
        "XACK mystream group1 123123 111",
        {"command": "XACK", "key": "mystream", "group": "group1", "stream_id": "111"},
    )


def test_xinfo(judge_command):
    judge_command(
        "XINFO consumers mystream mygroup",
        {
            "command": "XINFO",
            "stream_consumers": "consumers",
            "key": "mystream",
            "group": "mygroup",
        },
    )
    judge_command(
        "XINFO GROUPS mystream",
        {"command": "XINFO", "stream_groups": "GROUPS", "key": "mystream"},
    )
    judge_command(
        "XINFO STREAM mystream",
        {"command": "XINFO", "stream": "STREAM", "key": "mystream"},
    )
    judge_command("XINFO HELP", {"command": "XINFO", "help": "HELP"})
    judge_command("XINFO consumers mystream mygroup GROUPS mystream", None)
    judge_command("XINFO groups mystream mygroup", None)


def test_xpending(judge_command):
    judge_command(
        "XPENDING mystream group55",
        {"command": "XPENDING", "key": "mystream", "group": "group55"},
    )
    judge_command(
        "XPENDING mystream group55 myconsumer",
        {
            "command": "XPENDING",
            "key": "mystream",
            "group": "group55",
            "consumer": "myconsumer",
        },
    )
    judge_command(
        "XPENDING mystream group55 - + 10",
        {
            "command": "XPENDING",
            "key": "mystream",
            "group": "group55",
            "stream_id": ["-", "+"],
            "count": "10",
        },
    )
    judge_command(
        "XPENDING mystream group55 - + 10 myconsumer",
        {
            "command": "XPENDING",
            "key": "mystream",
            "group": "group55",
            "stream_id": ["-", "+"],
            "count": "10",
            "consumer": "myconsumer",
        },
    )
    judge_command("XPENDING mystream group55 - + ", None)
