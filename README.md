# ev-battery-thermal-management
A new project that includes real requirements: Battery Thermal Management System (BTMS) Logic
### Real-World Requirements (The "Spec"):
    REQ-01: The system shall monitor battery temperature ($T_{bat}$).
    REQ-02: If Tbat>45∘CTbat​>45∘C, the Cooling System must be activated (State: COOLING).
    REQ-03: If Tbat<10∘CTbat​<10∘C, the Battery Heater must be activated (State: HEATING).
    REQ-04: If 10∘C≤Tbat≤45∘C10∘C≤Tbat​≤45∘C, the system remains IDLE.
    REQ-05: If Tbat>60∘CTbat​>60∘C, the system must trigger a CRITICAL_SHUTDOWN.
