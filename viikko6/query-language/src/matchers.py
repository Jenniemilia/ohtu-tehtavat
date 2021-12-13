

class All:
    def matches(self, player):
        return True

class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def matches(self, player):
        return not self._matcher.matches(player)

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        
        return False

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value        
        self._attr = attr
    
    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class QueryBuilder:
    def __init__(self, stack = All()):
        self.build_object = stack

    def playsIn(self, team):
        matcher = And(self.build_object, PlaysIn(team))
        return QueryBuilder(matcher)

    def hasAtLeast(self, value, attr):
        matcher = And(self.build_object, HasAtLeast(value, attr))
        return QueryBuilder(matcher)

    def hasFewerThan(self, value, attr):
        matcher = And(self.build_object, HasFewerThan(value, attr))
        return QueryBuilder(matcher)

    def build(self):
        return self.build_object
