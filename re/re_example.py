import re

"""
match()

Determine if the RE matches at the beginning of the string.

search()

Scan through a string, looking for any location where this RE matches.

findall()

Find all substrings where the RE matches, and returns them as a list.

finditer()

Find all substrings where the RE matches, and returns them as an iterator.
"""


def checking_substring(s, sub):
    return sub in s, s.index(sub), s.find(sub)


def re_compile_example():
    p = re.compile(r"[a-z]+")
    print(p.match(""))
    print(p.match("abc"))

    match_obj = p.match("python")
    print("group dict: ", match_obj.groupdict())
    print("group: ", match_obj.group())
    print("groups: ", match_obj.groups())
    print("start: ", match_obj.start())
    print("end: ", match_obj.end())
    print("span: ", match_obj.span())

    m = p.match("")
    if m:
        print(m.group())
    else:
        print("there is no match")

    p = re.compile(r"\d+")
    print(p.findall("11 drummers went to 3 bars to drink 45 cups of beer"))
    for match in p.finditer("123 fgh 45 dhjkl 78"):
        print(match.span())
        print(match.group())


def re_module_example():
    print(re.match(r"From\s+", "Fromage amk"))
    print(re.match(r"From\s+", "From amk Thu May 14 19:12:10 1998"))

    # . - A period. Matches any single character except newline character.
    print(re.search(r"Co.k.e", "Cookie"))

    # \w - Lowercase w. Matches any single letter, digit or underscore.
    print(re.search(r"Co.k.e", "Cookie").group())

    # \W - Uppercase w. Matches any character not part of \w (lowercase w).
    print(re.search(r"C\Wo.\we", "C@okie"))

    # \s - Lowercase s. Matches a single whitespace character like: space, newline, tab, return
    print(re.search(r".\s\w+\s.*", "I am Vlad").group())

    # \S - Uppercase s. Matches any character not part of \s (lowercase s).
    print(re.search(r"Co\Skie", "Cookie").group())

    # \t - Lowercase t. Matches tab.
    print(re.search(r"Cookie\trules", "Cookie\trules"))

    #   \n - Lowercase n. Matches newline.
    #   \r - Lowercase r. Matches return.
    #   \d - Lowercase d. Matches decimal digit 0-9. \D is opposite

    print(re.search(r"C\d\dkie", "C00kie").group())
    # ^ - Caret. Matches a pattern at the start of the string. ( \A - in multiline mode )

    print(re.search(r"^Eat", "Eat cake").group())

    # $ - Matches a pattern at the end of string ( \Z - in multiline mode ).
    re.search(r"cake$", "Eat cake").group()

    # [abc] - Matches a or b or c.
    # [a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9).
    # Characters that are not within a range
    # can be matched by complementing the set.
    # If the first character of the set is ^, all the characters that are not in the set will be matched.

    print(re.search(r"Number: [0-5]", "Number: 4").group())
    print(re.search(r"^\w*\:\s[^5]$", "Number: 6").group())

    p = re.compile(r"^\w*\:\s[^5]$")
    print(p.search("num: 4").group())
    print(p.search("number: 6").group())
    print(p.search("NumBer: 1").group())
    print(p.search("NumBer: 5"))

    # \b - Lowercase b. Matches only the beginning or end of the word. ( \B - opposite )
    print(re.search(r"\w+\s\b\d+\b", "number 123"))


def repetitions():
    # + - Checks for one or more characters to its left.
    print(re.search(r"Co+kie", "Cooookie").group())

    # * - Checks for zero or more characters to its left.
    print(re.search(r"Ca*o*kie", "Caokie").group())

    # ? - Checks for exactly zero or one character to its left.
    print(re.search(r"Colou?r", "Color").group())

    # {x} - Repeat exactly x number of times.
    #
    # {x,} - Repeat at least x times or more.
    #
    # {x, y} - Repeat at least x times but no more than y times.

    print(re.search(r"\d{9,10}", "0987654321").group())


def groups():
    email = "contact us at: support-team@gmail.com"
    p = re.compile(r"([\d\w\.\-_]+)@([\w\.]+)")
    match = p.search(email)
    if match:
        print("group: ", match.group())
        print("group(1): ", match.group(1))
        print("group(2): ", match.group(2))
        print("groups(): ", match.groups())


def groups1():
    # the following example matches one or more occurrences of the string 'bar':
    print(re.search("(bar)+", "foo bar baz"))
    print(re.search("(bar)+", "foo barbar baz"))

    # The regex (ba[rz]){2,4}(qux)? matches 2 to 4 occurrences of either 'bar' or 'baz', optionally followed by 'qux':
    print(re.search("(ba[rz]){2,4}(qux)?", "bazbarbazqux"))
    print(re.search("(ba[rz]){2,4}(qux)?", "barbar"))

    # The following example shows that you can nest grouping parentheses:
    m = re.search("(foo(bar)?)+(\d\d\d)?", "foofoobar123")
    print(m.groups())


def greedy_vs_non_greedy():
    heading = r"<h1>TITLE</h1>"
    # The pattern <.*> matched the whole string, right up to the second occurrence of >
    print(re.match(r"<.*>", heading).group())
    print(re.match(r"<.+>", heading).group())

    # *? that matches as little text as possible.
    print(re.match(r"<.*?>", heading).group())
    print(re.match(r"<.+?>", heading).group())


def other_methods():
    email = "contact us via : tech_support@gmail.com, client-support@ukr.net"
    p = re.compile(r"[\w\-_\.]+@[\w\.]+")
    for match in p.findall(email):
        print(match)

    for match in p.finditer(email):
        print(match.group())

    email_new = re.sub(r"support", "contact", email)
    print(email_new)


if __name__ == "__main__":
    print(checking_substring("foo123cg", "123"))
    re_compile_example()
    re_module_example()
    repetitions()
    groups()
    greedy_vs_non_greedy()
    other_methods()
    groups1()
