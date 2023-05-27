set term svg enhanced mouse size 1280,720
set xdata time
set timefmt "%Y-%m"
set xrange ["2023-01":"2024-12"]
set xtics nomirror "2023-01",2592000 format "%b"
unset mxtics
set mytics 2
set grid xtics ytics mytics
set title "Movimientos"
set ylabel "Ingresos y gastos acumulados"
set style fill transparent solid 0.6 noborder
plot "includes/plots/datainput/incomes.txt" using 1:2 with filledcurves x1 title "Ingresos" linecolor rgb "light-salmon", '' using 1:2:2 with labels font "Courier,8" offset 0,0.5 textcolor linestyle 0 notitle, "includes/plots/datainput/expenses.txt" using 1:2 with filledcurves y1=0 title "Gastos" linecolor rgb "seagreen", '' using 1:2:2 with labels font "Courier,8" offset 0,0.5 textcolor linestyle 0 notitle
