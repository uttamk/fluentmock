#   fluentmock
#   Copyright 2013 Michael Gruber
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

from unittest import TestCase

from fluentmock import when, unstub, verify

import targetpackage


class ExampleTest(TestCase):

    def test_should_return_configured_value_three_when_called(self):
        when(targetpackage).targetfunction().then_return(3)

        self.assertEqual(3, targetpackage.targetfunction())

        verify(targetpackage).targetfunction()

        unstub()
