from numpy import array, linspace
import matplotlib.pyplot as plt
import funcs

health_red = array([200, 50, 50]) / 255
shield_blu = array([15, 215, 250]) / 255
armor_gold = array([230, 165, 40]) / 255


def fplot(ax, func, interval, params):
    x = linspace(interval[0], interval[1], 2 * (interval[1] - interval[0] + 1))
    y = func(x)
    return ax.plot(x, y, **params)


def pre_set(fig, ax, bl, title, ylabel, base=True):
    if base:
        ax.set_title(f"{title}\nBase Level = {bl}", fontsize=16, fontweight="bold")
    else:
        ax.set_title(title, fontsize=16, fontweight="bold")

    ax.set_xlabel("Current Level", fontsize=16)
    fig.tight_layout(pad=0)
    ax.set_ylabel(ylabel, fontsize=16)


def post_set(ax, start, end, ystart=1, legend=True, log=False):
    ax.set(xlim=[start, end], ylim=[ystart, ax.get_ylim()[1]])

    if not log:
        xticks = ax.get_xticks()
        xticks[0] = start
        ax.set_xticks(xticks)

    yticks = ax.get_yticks()
    yticks[0] = ystart
    ax.set_yticks(yticks)

    ax.grid(True)
    if legend:
        ax.legend()
    if log:
        ax.grid(True, which="minor")
        ax.set_xscale("log")


def plots():
    start = 1
    end = 200

    # Enemy Stat Scaling
    fig, ax = plt.subplots()
    pre_set(fig, ax, start, "Enemy Stat Scaling", "Base Stat Multiplier")

    params = {"label": "Health Scaling", "color": health_red, "linewidth": 2}
    fplot(ax, funcs.normal_health(1), [start, end], params)

    params = {"label": "Shield Scaling", "color": shield_blu, "linewidth": 2}
    fplot(ax, funcs.normal_shield(1), [start, end], params)

    params = {"label": "Armor Scaling", "color": armor_gold, "linewidth": 2}
    fplot(ax, funcs.normal_armor(1), [start, end], params)

    post_set(ax, start, end)

    # Enemy Eximus Stat Scaling
    fig, ax = plt.subplots()
    pre_set(fig, ax, start, "Eximus Stat Scaling", "Base Stat Multiplier")

    params = {"label": "Health Scaling", "color": health_red, "linewidth": 2}
    fplot(ax, funcs.eximus_health(1), [start, end], params)

    params = {"label": "Shield Scaling", "color": shield_blu, "linewidth": 2}
    fplot(ax, funcs.eximus_shield(1), [start, end], params)

    params = {"label": "Armor Scaling", "color": armor_gold, "linewidth": 2}
    fplot(ax, funcs.eximus_armor(1), [start, end], params)

    post_set(ax, start, end)

    # Enemy Health Scaling
    fig, ax = plt.subplots()
    pre_set(fig, ax, start, "Enemy Health Scaling", "Base Health Multiplier")

    params = {"label": "Normal", "color": health_red, "linewidth": 2}
    fplot(ax, funcs.normal_health(1), [start, end], params)

    params = {"label": "Eximus", "color": health_red, "linestyle": ":", "linewidth": 2}
    fplot(ax, funcs.eximus_health(1), [start, end], params)

    post_set(ax, start, end)

    # Enemy Shield Scaling
    fig, ax = plt.subplots()
    pre_set(fig, ax, start, "Enemy Shield Scaling", "Base Shield Multiplier")

    params = {"label": "Normal", "color": shield_blu, "linewidth": 2}
    fplot(ax, funcs.normal_shield(1), [start, end], params)

    params = {"label": "Eximus", "color": shield_blu, "linestyle": ":", "linewidth": 2}
    fplot(ax, funcs.eximus_shield(1), [start, end], params)

    post_set(ax, start, end)

    # Enemy Armor Scaling
    fig, ax = plt.subplots()
    pre_set(fig, ax, start, "Enemy Armor Scaling", "Base Armor Multiplier")

    params = {"label": "Normal", "color": armor_gold, "linewidth": 2}
    fplot(ax, funcs.normal_armor(1), [start, end], params)

    params = {"label": "Eximus", "color": armor_gold, "linestyle": ":", "linewidth": 2}
    fplot(ax, funcs.eximus_armor(1), [start, end], params)

    post_set(ax, start, end)

    # Enemy Overguard Scaling
    fig, ax = plt.subplots()
    pre_set(fig, ax, start, "Enemy Overguard Scaling", "Base Overguard Multiplier")

    params = {"label": "Eximus", "linewidth": 2}
    fplot(ax, funcs.eximus_overguard(1), [start, end], params)

    post_set(ax, start, end, legend=False)

    # Enemy Damage Scaling
    fig, ax = plt.subplots()
    pre_set(fig, ax, start, "Enemy Damage Scaling", "Base Damage Multiplier")

    params = {"label": "Normal", "linewidth": 2}
    fplot(ax, funcs.normal_damage(1), [start, end], params)

    post_set(ax, start, end, legend=False)

    # Enemy Affinity Scaling
    fig, ax = plt.subplots()
    pre_set(fig, ax, start, "Enemy Affinity Scaling", "Base Affinity Multiplier", base=False)

    params = {"label": "Normal", "linewidth": 2}
    fplot(ax, funcs.normal_affinity(), [start, end], params)

    params = {"label": "Eximus", "linewidth": 2}
    fplot(ax, funcs.eximus_affinity(), [start, end], params)

    post_set(ax, start, end)

    # Enemy Shield Ratio Scaling
    end = 200
    log = False
    fig, ax = plt.subplots()
    pre_set(fig, ax, start, "Enemy Shield Ratio Scaling", "Shield to Health Ratio")

    params = {"label": "Normal", "linewidth": 2}
    fplot(ax, funcs.normal_shield_ratio(1), [start, end], params)

    params = {"label": "Eximus", "linewidth": 2}
    fplot(ax, funcs.eximus_shield_ratio(1), [start, end], params)

    post_set(ax, start, end, ystart=0, log=log)

    # Enemy Affinity Density Scaling
    fig, ax = plt.subplots()
    pre_set(fig, ax, start, "Enemy AD Scaling", "Base AD Multiplier")

    params = {"label": "Normal", "linewidth": 2}
    fplot(ax, funcs.normal_affinity_density(1), [start, end], params)

    params = {"label": "Eximus", "linewidth": 2}
    fplot(ax, funcs.eximus_affinity_density(1), [start, end], params)

    post_set(ax, start, end, ystart=0, log=log)

    # Enemy RKR Scaling
    fig, ax = plt.subplots()
    pre_set(fig, ax, start, "Enemy RKR Scaling", "Base RKR Multiplier")

    params = {"label": "Normal", "linewidth": 2}
    fplot(ax, funcs.normal_rkr(1), [start, end], params)

    params = {"label": "Eximus", "linewidth": 2}
    fplot(ax, funcs.eximus_rkr(1), [start, end], params)

    post_set(ax, start, end, ystart=0, log=log)

    plt.show()


if __name__ == "__main__":
    plots()
