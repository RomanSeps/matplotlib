# matplotlib

Knihovna Matplotlib slouží k vykreslování grafů v jazyce Python, od běžných čar po různé grafické obrazce.

Nejprve si knihovnu importujeme, poté určíme body jako např.: "xpoints = np.array([0, 6])", poté už pouze graf

zobrazíme pomocí příkazu: "plt.show". V knihovně Matplotlib však můžeme různě grafy upravovat, můžeme měnit 

barvu "color = 'r'", typ čáry "ls = ':'", můžeme přidávat titulky a podtitulky "plt.title("titulek")"

"plt.xlabel("podtitulek")", 

mřížky "plt.grid()", či kompletně změnit tvar grafu např: "plt.pie(ypoints)" tvar koláče. Můžeme přidávat

podtabulky "plt.subplot", atd. Tento program nejprve určí několik bodů, upraví je, poté z nich vytvoří grafy

a nakonec přidá mřížku a vše zobrazí.    
