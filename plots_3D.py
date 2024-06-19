from numpy import geomspace, linspace, log10, meshgrid
import matplotlib.pyplot as plt
import funcs


def surface(ax, func, interval, interval2, params, log=False):
    maxint = 200
    y = linspace(interval2[0], interval2[1], maxint)
    if log:
        x = geomspace(interval[0], interval[1], maxint)
    else:
        x = linspace(interval[0], interval[1], maxint)
    X, Y = meshgrid(x, y)
    Z = func(X, Y)
    x = linspace(interval[0], interval[1], maxint)
    X, _ = meshgrid(x, y)

    ax.plot_surface(X, Y, Z, alpha=0.3, linewidth=0, **params)
    ax.contour3D(X, Y, Z, 100, **params)
    ax.set(xlim=[x[0], x[-1]], ylim=[y[0], y[-1]])

    xticks = ax.get_xticks()
    xticks[0] = X.min()
    ax.set_xticks(xticks)

    yticks = ax.get_yticks()
    yticks[0] = Y.min()
    ax.set_yticks(yticks)

    ax.grid(True)
    return Z


def pre_set(ax, title, ylabel, zlabel):
    ax.set_title(title, fontsize=16, fontweight="bold")
    ax.set_xlabel("Current Level", fontsize=16)
    ax.set_ylabel(ylabel, fontsize=16)
    ax.set_zlabel(zlabel, fontsize=16)
    ax.grid(True)


def post_set(fig, ax1, ax2, z1, z2, log=False, interval=None):
    ax1.set(zlim=[min(z1.min(), z2.min()), max(z1.max(), z2.max())])
    ax2.set(zlim=[min(z1.min(), z2.min()), max(z1.max(), z2.max())])

    zticks = ax1.get_zticks()
    zticks[0] = min(z1.min(), z2.min())
    ax1.set_zticks(zticks)
    zticks = ax2.get_zticks()
    zticks[0] = min(z1.min(), z2.min())
    ax2.set_zticks(zticks)

    color = (0.5, 0.5, 0.5, 1.0)
    ax1.w_xaxis.set_pane_color(color)
    ax1.w_yaxis.set_pane_color(color)
    ax1.w_zaxis.set_pane_color(color)
    ax2.w_xaxis.set_pane_color(color)
    ax2.w_yaxis.set_pane_color(color)
    ax2.w_zaxis.set_pane_color(color)

    fig.tight_layout(h_pad=0.0)

    if log:
        x = linspace(interval[0], interval[1], int(log10(interval[1])) + 1)
        x2 = linspace(int(log10(interval[0])), int(log10(interval[1])), int(log10(interval[1])) + 1)
        ax1.set_xticks(x, [f"$10^{{{int(val)}}}$" for val in x2])
        ax2.set_xticks(x, [f"$10^{{{int(val)}}}$" for val in x2])


def plots():
    cmap = "CMRmap"
    start = 1
    end = 200

    # Enemy EHP Scaling (Shields)
    print("Making `Enemy EHP Scaling (Shields)`...")
    fig = plt.figure()
    fig.suptitle(f"Enemy EHP Scaling (Shields, no Armor)\nBase Level = {start}", fontsize=16, fontweight="bold")

    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    pre_set(ax1, "Eximus", "Base Shields to Health Ratio", "EHP Multiplier")
    ax1.view_init(35, -120)
    params = {"label": "Eximus Scaling", "cmap": cmap}
    z1 = surface(ax1, funcs.eximus_EHP_shield(1), [start, end], [0, 3], params)

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    pre_set(ax2, "Normal", "Base Shields to Health Ratio", "EHP Multiplier")
    ax2.view_init(35, -120)
    params = {"label": "Normal Scaling", "cmap": cmap}
    z2 = surface(ax2, funcs.normal_EHP_shield(1), [start, end], [0, 3], params)

    post_set(fig, ax1, ax2, z1, z2)
    print("    Done.")

    # Enemy EHP Scaling (Armor)
    print("Making `Enemy EHP Scaling (Armor)`...")
    fig = plt.figure()
    fig.suptitle(f"Enemy EHP Scaling (Armor, no Shields)\nBase Level = {start}", fontsize=16, fontweight="bold")

    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    pre_set(ax1, "Eximus", "Base Armor", "EHP Multiplier")
    ax1.view_init(35, -120)
    params = {"label": "Eximus Scaling", "cmap": cmap}
    z1 = surface(ax1, funcs.eximus_EHP_armor(1), [start, end], [0, 500], params)

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    pre_set(ax2, "Normal", "Base Armor", "EHP Multiplier")
    ax2.view_init(35, -120)
    params = {"label": "Normal Scaling", "cmap": cmap}
    z2 = surface(ax2, funcs.normal_EHP_armor(1), [start, end], [0, 500], params)

    post_set(fig, ax1, ax2, z1, z2)
    print("    Done.")

    # Enemy Shield Ratio Scaling
    print("Making `Enemy Shield Ratio Scaling`...")
    end = 200
    log = False
    fig = plt.figure()
    fig.suptitle(f"Enemy Shield Ratio Scaling\nBase Level = {start}", fontsize=16, fontweight="bold")

    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    pre_set(ax1, "Eximus", "Base Armor", "Shield Ratio Multiplier")
    ax1.view_init(35, 60)
    params = {"label": "Eximus Scaling", "cmap": cmap}
    z1 = surface(ax1, funcs.eximus_shield_ratio_armor(1), [start, end], [0, 500], params, log=log)

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    pre_set(ax2, "Normal", "Base Armor", "Shield Ratio Multiplier")
    ax2.view_init(35, 60)
    params = {"label": "Normal Scaling", "cmap": cmap}
    z2 = surface(ax2, funcs.normal_shield_ratio_armor(1), [start, end], [0, 500], params, log=log)

    post_set(fig, ax1, ax2, z1, z2, log=log, interval=[start, end])
    print("    Done.")

    # Enemy Affinity Density Scaling (Shields)
    print("Making `Enemy AD Scaling (Shields)`...")
    fig = plt.figure()
    fig.suptitle(f"Enemy AD Scaling (Shields, no Armor)\nBase Level = {start}", fontsize=16, fontweight="bold")

    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    pre_set(ax1, "Eximus", "Base Shields to Health Ratio", "Base AD Multiplier")
    ax1.view_init(35, 60)
    params = {"label": "Eximus Scaling", "cmap": cmap}
    z1 = surface(ax1, funcs.eximus_affinity_density_shield(1), [start, end], [0, 3], params, log=log)

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    pre_set(ax2, "Normal", "Base Shields to Health Ratio", "Base AD Multiplier")
    ax2.view_init(35, 60)
    params = {"label": "Normal Scaling", "cmap": cmap}
    z2 = surface(ax2, funcs.normal_affinity_density_shield(1), [start, end], [0, 3], params, log=log)

    post_set(fig, ax1, ax2, z1, z2, log=log, interval=[start, end])
    print("    Done.")

    # Enemy Affinity Density Scaling (Armor)
    print("Making `Enemy AD Scaling (Armor)`...")
    fig = plt.figure()
    fig.suptitle(f"Enemy AD Scaling (Armor, no Shields)\nBase Level = {start}", fontsize=16, fontweight="bold")

    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    pre_set(ax1, "Eximus", "Base Armor", "Base AD Multiplier")
    ax1.view_init(35, 60)
    params = {"label": "Eximus Scaling", "cmap": cmap}
    z1 = surface(ax1, funcs.eximus_affinity_density_armor(1), [start, end], [0, 500], params, log=log)

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    pre_set(ax2, "Normal", "Base Armor", "Base AD Multiplier")
    ax2.view_init(35, 60)
    params = {"label": "Normal Scaling", "cmap": cmap}
    z2 = surface(ax2, funcs.normal_affinity_density_armor(1), [start, end], [0, 500], params, log=log)

    post_set(fig, ax1, ax2, z1, z2, log=log, interval=[start, end])
    print("    Done.")

    # Enemy RKR Scaling (Shields)
    print("Making `Enemy RKR Scaling (Shields)`...")
    fig = plt.figure()
    fig.suptitle(f"Enemy RKR Scaling (Shields, no Armor)\nBase Level = {start}", fontsize=16, fontweight="bold")

    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    pre_set(ax1, "Eximus", "Base Shields to Health Ratio", "Base RKR Multiplier")
    ax1.view_init(35, 60)
    params = {"label": "Eximus Scaling", "cmap": cmap}
    z1 = surface(ax1, funcs.eximus_rkr_shield(1), [start, end], [0, 3], params, log=log)

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    pre_set(ax2, "Normal", "Base Shields to Health Ratio", "Base RKR Multiplier")
    ax2.view_init(35, 60)
    params = {"label": "Normal Scaling", "cmap": cmap}
    z2 = surface(ax2, funcs.normal_rkr_shield(1), [start, end], [0, 3], params, log=log)

    post_set(fig, ax1, ax2, z1, z2, log=log, interval=[start, end])
    print("    Done.")

    # Enemy RKR Scaling (Armor)
    print("Making `Enemy RKR Scaling (Armor)`...")
    fig = plt.figure()
    fig.suptitle(f"Enemy RKR Scaling (Armor, no Shields)\nBase Level = {start}", fontsize=16, fontweight="bold")

    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    pre_set(ax1, "Eximus", "Base Armor", "Base RKR Multiplier")
    ax1.view_init(35, 60)
    params = {"label": "Eximus Scaling", "cmap": cmap}
    z1 = surface(ax1, funcs.eximus_rkr_armor(1), [start, end], [0, 500], params, log=log)

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    pre_set(ax2, "Normal", "Base Armor", "Base RKR Multiplier")
    ax2.view_init(35, 60)
    params = {"label": "Normal Scaling", "cmap": cmap}
    z2 = surface(ax2, funcs.normal_rkr_armor(1), [start, end], [0, 500], params, log=log)

    post_set(fig, ax1, ax2, z1, z2, log=log, interval=[start, end])
    print("    Done.")

    plt.show()


if __name__ == "__main__":
    plots()
