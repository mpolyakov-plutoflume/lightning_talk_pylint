import astroid
import not_odd_plugin
import pylint.testutils


class TestNotOddChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = not_odd_plugin.NotOddChecker

    def test_good(self):
        node = astroid.extract_node(
            """
        x = 2 #@
        """
        )

        with self.assertNoMessages():
            self.checker.visit_assign(node)

    def test_bad(self):
        node = astroid.extract_node(
            """
        x = 1 #@
        """
        )

        with self.assertAddsMessages(
            pylint.testutils.MessageTest(
                msg_id="not-odd",
                node=node,
            ),
            ignore_position=True,
        ):
            self.checker.visit_assign(node)

    def test_call(self):
        node = astroid.extract_node(
            """
        def foo():
            return 1
        x = foo() #@
        """
        )

        with self.assertAddsMessages(
            pylint.testutils.MessageTest(
                msg_id="not-odd",
                node=node,
            ),
            ignore_position=True,
        ):
            self.checker.visit_assign(node)
