/*
Falling object

m dv/dt = m g - c v² , v(0) = 0
*/

#include <stdio.h>
#include <math.h>

#define STEPS 40

static const double m = 70.0; // mass, kg
static const double c = 0.30; // drag coefficient, kg/m
static const double g = 9.81; // gravity m/s²
static const double dt = 0.5; // changing in time , time step s

double acceleration(double v)
{
    return g - (c / m) * v * v; /* v²*/
}

double exact_speed(double t)
{
    double vt = sqrt(m * g / c);
    return vt * tanh(g * t / vt);
}

int main()
{
        double t[STEPS + 1], v[STEPS + 1];

    t[0] = 0.0;
    v[0] = 0.0;
    for (int n = 0; n < STEPS; n++) {
        v[n + 1] = v[n] + dt * acceleration(v[n]);
        t[n + 1] = (n + 1) * dt;
    }

    printf("%6s %10s %10s %10s\n", "t (s)", "v_Euler", "v_exact", "error");
    for (int n = 0; n <= STEPS; n += 4) {
        double ve = exact_speed(t[n]);
        printf("%6.1f %10.4f %10.4f %10.2e\n", t[n], v[n], ve, v[n] - ve);
    }
    printf("Terminal velocity: %.4f m/s\n", sqrt(m * g / c));
    return 0;
}
