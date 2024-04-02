% Run from octave command window

clc;  % Clear command history
close all;  % Close all windows
clear all;  % Clear variables


%% ******************** First approach ******************
z = 0: .1 : 12;  % Array from 0 to 12 with steps of.1
k = sin(z);

figure(1)  % Create figure
plot(z, k)

%% ******************** Second approach ******************
clear; clc;

T = 2 * pi;  % Period (s)
tf = 3 * T;  % End time (s)
t = 0: T / 20: tf;  % Time array (s)
w = 2 * pi / T;  % frequency (rad/s)
A = 1;  % Max amplitude (m)
x = sin(w * t);  % Position (m)

figure(2)
plot(t, x)

ylabel('x (m)')
xlabel('t (s)')
axes_handler = gca;  % gca: "get current axes"
set(axes_handler, 'FontSize',12);
title('Sine wave plot', 'FontSize', 20)


%% ******************** Third approach ******************
figure_handler = figure(3);
plot(t, x)

ylabel('x (m)')
xlabel('t (s)')
title('Sine wave plot with custom ticks')

xlim([0 6*pi]);
xticks([0: pi: tf])
xticklabels({'0','\pi','2\pi','3\pi','4\pi','5\pi','6\pi'})

ax = gca;
set(ax,'FontSize',12);

print(figure_handler, '-dpng', 'img/sine_octave.png')
