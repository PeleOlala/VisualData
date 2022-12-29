"""
project2 Visual Data
"""
import matplotlib.pyplot as plt
from mouvement_brownien import BrownienMouve

if __name__ == '__main__':
    bm = BrownienMouve(50000)
    while True:
        bm.fill_walk()
        #    x_v = range(1,1001) #[1, 4, 9, 16, 25]
        #    y_v = [x**2 for x in x_v]#[1, 2, 3, 4, 5]
        plt.style.use("dark_background")
        fig, ax = plt.subplots(figsize=(10,6), dpi=400)
        point_numbres = range(bm.num_pointes)
        ax.scatter(bm.x_values, bm.y_values, s=1,
                   c=point_numbres, cmap=plt.cm.Blues, edgecolors='none')
        ax.scatter(0,0, c='green', edgecolors='none', s=10)
        ax.scatter(bm.x_values[-1],bm.y_values[-1], c='red', edgecolors='none', s=10)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        # ax.plot(input_value, carre, linewidth=3)
        # Задати назву графіка та кожної осі
        ax.set_title("Chiffres de carré", fontsize=24)
        ax.set_xlabel("Value", fontsize=14)
        ax.set_ylabel("Carré de value", fontsize=14)
        # Розмір підписів на розмітці
        ax.tick_params(axis='both', labelsize=14)
        #    ax.axis([0, 1100, 0, 1100000])
        plt.show()
        #   plt.savefig('test.png', bbox_inches='tight')
        keep_run = input("Continu?")
        if keep_run == 'n':
            break
