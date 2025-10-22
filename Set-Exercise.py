maths = {"Emma", "Leon", "Sofia", "Noah", "Mia"}
science = {"Noah", "Elias", "Emma", "Ben", "Lea"}
english = {"Mia", "Leon", "Ben", "Emma", "Paul"}

m_a_s = maths.intersection(science)

print(m_a_s.difference(english))


m = maths.difference(english)
print(m.difference(science))


c = maths.intersection(science)
print(c.intersection(english))

i = (maths.intersection(science)).difference(english)
i2 = (maths.intersection(english)).difference(science)
i3 = (science.intersection(english)).difference(maths)

print((i.union(i2)).union(i3))

r = ((maths.union(science)).union(english)).difference((maths.intersection(science)).intersection(english))
print(r)



