from linter.rule import Rule
from linter.severity import Severity


class DimensionGroupOfTypeTimeRequiresTimeframe(Rule):
    def default_severity():
        return Severity.WARNING.value

    def applies_to():
        return ('dimension_group',)

    def run(self, dimension_group):
        type = dimension_group.get('type')
        if type == 'time' and not 'timeframe' in dimension_group:
            return False
        return True