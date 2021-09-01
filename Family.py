class Father(object):
    father_name = ""
    father_age = None

    def __init__(self):
        pass

    def set_father_name(self, name):
        self.father_name = name

    def set_father_age(self, age):
        self.father_age = age

    def get_father_name(self):
        return self.father_name

    def get_father_age(self):
        return self.father_age


class Mother(object):
    mother_name = ""
    mother_age = None

    def __init__(self):
        pass

    def set_mother_name(self, name):
        self.mother_name = name

    def set_mother_age(self, age):
        self.mother_age = age

    def get_mother_name(self):
        return self.mother_name

    def get_mother_age(self):
        return self.mother_age


class Child(Father, Mother):
    child_name = ""
    child_age = None
    father = Father()
    mother = Mother()

    def __init__(self):
        pass

    def set_child_name(self, name):
        self.child_name = name

    def set_child_age(self, age):
        self.child_age = age

    def set_father(self, name, age):
        self.father.set_father_name(name)
        self.father.set_father_age(age)

    def set_mother(self, name, age):
        self.mother.set_mother_name(name)
        self.mother.set_mother_age(age)

    def get_child_name(self):
        return self.child_name

    def get_child_age(self):
        return self.child_age

    def set_parents(self, father_details, mother_details):
        self.set_father(father_details['name'], father_details['age'])
        self.set_mother(mother_details['name'], mother_details['age'])


class Family(Child):
    parents = dict()
    children = dict()
    last_name = ""

    def __init__(self, parents: dict, children: dict, last_name=''):
        self.parents = parents
        for k, v in children.items():
            self.add_child(k, v)
        self.last_name = last_name

    def add_child(self, child_name, child_age):
        self.set_child_name(child_name)
        self.set_child_age(child_age)
        self.set_parents(self.parents['father'], self.parents['mother'])
        self.children[self.child_name] = self.child_age

    def get_child(self, i):
        tmp = list()
        for k, v in self.children.items():
            tmp.append((v, k))
        v, k = tmp[i - 1]
        return k, v

    def get_children(self):
        return self.children

    def get_parents_names(self):
        father, mother = (v['name'] for k, v in self.parents.items())
        return father, mother
