#   fluentmock
#   Copyright 2013-2014 Michael Gruber
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


class FluentMatcher(object):

    def matches(self, value):
        raise NotImplementedError()

    def _matcher_string(self, text):
        return '<< {text} >>'.format(text=text)

    def __repr__(self):
        raise NotImplementedError()


class AnyValuesMatcher(FluentMatcher):

    def matches(self, value):
        return True

    def __repr__(self):
        return self._matcher_string('ANY_VALUES')


class AnyValueMatcher(FluentMatcher):

    def matches(self, value):
        return True

    def __repr__(self):
        return self._matcher_string('ANY_VALUE')


class AnyValueOfTypeMatcher(FluentMatcher):

    def __init__(self, expected_type):

        self._expected_type = expected_type

    def matches(self, value):

        if isinstance(value, self._expected_type):
            return True

        return False

    def __repr__(self):
        type_name = self._expected_type.__name__
        text = 'Any value of type "{type_name}"'.format(type_name=type_name)
        return self._matcher_string(text)


class ContainsMatcher(FluentMatcher):

    def __init__(self, substring):
        self._substring = substring

    def matches(self, value):
        return value.find(self._substring) >= 0

    def __repr__(self):
        text = 'a string containing "{substring}"'.format(substring=self._substring)
        return self._matcher_string(text)


class NeverMatcher(FluentMatcher):

    def matches(self, value):
        if value != 0:
            return False

        return True

    def __repr__(self):
        return self._matcher_string('should never be called')


class AtLeastOnceMatcher(FluentMatcher):

    def matches(self, value):

        if value == 0:
            return False

        return True

    def __repr__(self):
        return self._matcher_string('at least once')


class TimesMatcher(FluentMatcher):

    def __init__(self, expected):
        self._expected = expected

    def matches(self, value):

        if value != self._expected:
            return False

        return True

    def __repr__(self):
        text = 'exactly {expected} times'.format(expected=self._expected)
        return self._matcher_string(text)


def contains(substring):
    return ContainsMatcher(substring)


def any_value_of_type(the_type):
    return AnyValueOfTypeMatcher(the_type)
