from numpy import sqrt


def T(x, start, end):
    return (x - start) / (end - start)


def S(x, start, end):
    t = T(x, start, end)
    t[x < start] = 0
    t[x > end] = 1
    t2 = t * t
    return 3 * t2 - 2 * t * t2


def health_f1(bl):
    return lambda x: 1 + 0.015 * (x - bl) ** 2


def health_f2(bl):
    return lambda x: 1 + 24 * sqrt(5 * (x - bl)) / 5


def shield_f0(bl):
    return lambda x: 1 + 0.0075 * (x - bl) ** 2


def shield_f1(bl):
    return lambda x: 1 + 0.02 * (x - bl) ** 1.76


def shield_f2(bl):
    return lambda x: 1 + 2 * (x - bl) ** 0.76


def armor_f1(bl):
    return lambda x: 1 + 0.005 * (x - bl) ** 1.75


def armor_f2(bl):
    return lambda x: 1 + 0.4 * (x - bl) ** 0.75


def overguard_f1(bl):
    return lambda x: 1 + 0.0015 * (x - bl) ** 4


def overguard_f2(bl):
    return lambda x: 1 + 260 * (x - bl) ** 0.9


def normal_damage(bl):
    return lambda x: 1 + 0.015 * (x - bl) ** 1.55


def normal_affinity():
    return lambda x: 1 + 0.1425 * sqrt(x)


def normal_health(bl):
    return lambda x: health_f1(bl)(x) * (1 - S(x - bl, 70, 80)) + health_f2(bl)(x) * S(x - bl, 70, 80)


def normal_shield(bl):
    return lambda x: shield_f1(bl)(x) * (1 - S(x - bl, 70, 80)) + shield_f2(bl)(x) * S(x - bl, 70, 80)


def normal_armor(bl):
    return lambda x: armor_f1(bl)(x) * (1 - S(x - bl, 70, 80)) + armor_f2(bl)(x) * S(x - bl, 70, 80)


def normal_EHP_shield(bl):
    return lambda x, ratio: normal_health(bl)(x) + ratio * normal_shield(bl)(x)


def normal_EHP_armor(bl):
    return lambda x, armor: normal_health(bl)(x) * (1 + armor * normal_armor(bl)(x) / 300)


def normal_shield_ratio(bl):
    return lambda x: normal_shield(bl)(x) / normal_health(bl)(x)


def normal_shield_ratio_armor(bl):
    return lambda x, armor: normal_shield(bl)(x) / normal_EHP_armor(bl)(x, armor)


def normal_affinity_density(bl):
    return lambda x: normal_affinity()(x) / normal_health(bl)(x)


def normal_affinity_density_shield(bl):
    return lambda x, ratio: normal_affinity()(x) / normal_EHP_shield(bl)(x, ratio)


def normal_affinity_density_armor(bl):
    return lambda x, armor: normal_affinity()(x) / normal_EHP_armor(bl)(x, armor)


def normal_rkr(bl):
    return lambda x: normal_damage(bl)(x) / normal_health(bl)(x)


def normal_rkr_shield(bl):
    return lambda x, ratio: normal_damage(bl)(x) / normal_EHP_shield(bl)(x, ratio)


def normal_rkr_armor(bl):
    return lambda x, armor: normal_damage(bl)(x) / normal_EHP_armor(bl)(x, armor)


def eximus_health(bl):
    def f(x):
        x -= bl
        y = health_f1(0)(x)  # x <= 25
        y[25 < x] = (1.0 + 0.05 * (x[25 < x] - 25)) * health_f1(0)(x[25 < x])
        y[35 < x] = (1.5 + 0.10 * (x[35 < x] - 35)) * health_f1(0)(x[35 < x])
        y[50 < x] = (3.0 + 0.02 * (x[50 < x] - 50)) * normal_health(0)(x[50 < x])
        y[100 < x] = 4 * health_f2(0)(x[100 < x])
        x += bl
        return y

    return f


def eximus_shield(bl):
    def f(x):
        x -= bl
        y = shield_f1(0)(x)  # x <= 15
        y[15 < x] = (1.0 + 0.025 * (x[15 < x] - 15)) * shield_f1(0)(x[15 < x])
        y[25 < x] = (1.25 + 0.125 * (x[25 < x] - 25)) * shield_f1(0)(x[25 < x])
        y[35 < x] = (2.5 + (2/15) * (x[35 < x] - 35)) * shield_f1(0)(x[35 < x])
        y[50 < x] = (4.5 + 0.03 * (x[50 < x] - 50)) * normal_shield(0)(x[50 < x])
        y[100 < x] = 6 * shield_f2(0)(x[100 < x])
        x += bl
        return y

    return f


def eximus_armor(bl):
    def f(x):
        x -= bl
        y = armor_f1(0)(x)  # x <= 25
        y[25 < x] = (1.0 + 0.0125 * (x[25 < x] - 25)) * armor_f1(0)(x[25 < x])
        y[35 < x] = (1.125 + (2/30) * (x[35 < x] - 35)) * armor_f1(0)(x[35 < x])
        y[50 < x] = (1.375 + 0.005 * (x[50 < x] - 50)) * normal_armor(0)(x[50 < x])
        y[100 < x] = 1.625 * armor_f2(0)(x[100 < x])
        x += bl
        return y

    return f


def eximus_overguard(bl):
    return lambda x: overguard_f1(bl)(x) * (1 - S(x - bl, 45, 50)) + overguard_f2(bl)(x) * S(x - bl, 45, 50)


def eximus_damage(bl):
    return lambda x: 1 + 0.015 * (x - bl) ** 1.55


def eximus_affinity():
    return lambda x: 3 + 0.1425 * sqrt(x)


def eximus_EHP_shield(bl):
    return lambda x, ratio: eximus_health(bl)(x) + ratio * eximus_shield(bl)(x)


def eximus_EHP_armor(bl):
    return lambda x, armor: eximus_health(bl)(x) * (1 + armor * eximus_armor(bl)(x) / 300)


def eximus_EHP_overguard(bl):
    return lambda x, ratio: eximus_health(bl)(x) + ratio * eximus_overguard(bl)(x)


def eximus_shield_ratio(bl):
    return lambda x: eximus_shield(bl)(x) / eximus_health(bl)(x)


def eximus_shield_ratio_armor(bl):
    return lambda x, armor: eximus_shield(bl)(x) / eximus_EHP_armor(bl)(x, armor)


def eximus_shield_ratio_overguard(bl):
    return lambda x, overguard: eximus_shield(bl)(x) / eximus_EHP_overguard(bl)(x, overguard)


def eximus_affinity_density(bl):
    return lambda x: eximus_affinity()(x) / eximus_health(bl)(x)


def eximus_affinity_density_shield(bl):
    return lambda x, ratio: eximus_affinity()(x) / eximus_EHP_shield(bl)(x, ratio)


def eximus_affinity_density_armor(bl):
    return lambda x, armor: eximus_affinity()(x) / eximus_EHP_armor(bl)(x, armor)


def eximus_affinity_density_overguard(bl):
    return lambda x, overguard: eximus_affinity()(x) / eximus_EHP_overguard(bl)(x, overguard)


def eximus_rkr(bl):
    return lambda x: eximus_damage(bl)(x) / eximus_health(bl)(x)


def eximus_rkr_shield(bl):
    return lambda x, ratio: eximus_damage(bl)(x) / eximus_EHP_shield(bl)(x, ratio)


def eximus_rkr_armor(bl):
    return lambda x, armor: eximus_damage(bl)(x) / eximus_EHP_armor(bl)(x, armor)


def eximus_rkr_overguard(bl):
    return lambda x, overguard: eximus_damage(bl)(x) / eximus_EHP_overguard(bl)(x, overguard)
