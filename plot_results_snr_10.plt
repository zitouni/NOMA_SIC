set output "results/result_snr_10_with.eps"
set terminal postscript eps enhanced
#set   autoscale                        # scale axes automatically
set encoding utf8
unset log                              # remove any log-scaling
unset label                            # remove any previous labels
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set title "NOMA/SIC with an SNR=10dB"
set xlabel "{/Symbol a} amplifier P1/P"
set ylabel "Bit Error Rate (BER)"
set xr [0.0:1.0]
set yr [0.0:1.0]
set size 1,1

#set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5   # --- blue
#set style line 2 lc rgb '#dd181f' lt 1 lw 2 pt 5 ps 1.5   # --- red
#set style line 1 lc rgb '#00008B' lt 1 lw 2 pt 7 ps 1.5   # --- blue
#set style line 1 lc rgb '#708090' lt 1 lw 2 pt 7 ps 1.5   # --- slategray

set grid ytics lc rgb "#bbbbbb" lw 1 lt 0 # add grid view
set grid xtics lc rgb "#bbbbbb" lw 1 lt 0 # add grid view

#plot 'results/result_100_snr_10.0.txt' using 10:2 title 'User 1 BER without SIC' with linespoints lc rgb '#0060ad', \
#     'results/result_100_snr_10.0.txt' using 10:4 title 'User 1 BER with SIC' with linespoints lc rgb '#708090', 

plot 'results/result_100_snr_10.0.txt' using 10:4 title 'User 1 BER with SIC' with linespoints lc rgb '#dd181f', \
     'results/result_100_snr_10.0.txt' using 10:8 title 'User 2 BER with SIC' with linespoints, \
#     'results/result_100_snr_10.0.txt' using 10:8 title 'User 2 BER After SIC' with linespoints lc rgb '#708090', 
#     'results/result_100_snr_10.0.txt' using 10:2 title 'User 1 BER without SIC' with linespoints lc rgb '#dd181f', 
#plot 'results/result_100_snr_10.0.txt' using 10:2 title 'User 1 BER without SIC' with linespoints, \
#     'results/result_100_snr_10.0.txt' using 10:4 title 'User 1 BER After SIC' with linespoints, \
#     'results/result_100_snr_10.0.txt' using 10:8 title 'User 2 BER After SIC' with linespoints, 
					
