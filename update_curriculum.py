import re

with open('curriculum_ideas_v4.md', 'r') as f:
    content = f.read()

replacements = [
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Explain that a complete circuit path.*?Write a short 'what I measured, what it means' reflection to accompany logged data",
        """**Knowledge**
*Concepts ('know that')*
- A sensor converts a physical quantity into a voltage; this voltage is a claim about reality, not reality itself.
- Noise is the natural variation in sensor readings that occurs even when the physical quantity is constant.
- A complete circuit path is required for current to flow.

*Substantive Knowledge ('know about')*
- Voltage, current, and resistance are the fundamental properties of electrical circuits.
- Breadboards have specific internal connections that support circuit construction but can hide connection errors.

*Procedural Knowledge ('know how')*
- A multimeter is the primary diagnostic tool for checking continuity and source voltage.
- The serial monitor is used to observe microcontroller measurements in real time.
- A measurement log is a formal engineering record, not optional paperwork.

**Practices**
*Tools and Skills ('know how to use')*
- Use a multimeter to verify continuity and measure source voltage before connecting a microcontroller.
- Build an analogue sensor circuit (e.g., voltage divider) on a breadboard.
- Use the serial monitor to read and display sensor values.

*Application ('know how to apply')*
- Record a table of readings across at least three different physical conditions; describe what changes and what stays constant.
- Capture high and low sensor readings over a 30-second period to quantify the noise range.
- Write a 'what I measured, what it means' reflection to accompany logged data."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Identify and describe safety hazards.*?Record current draw \(or describe supply behaviour\) under different load conditions",
        """**Knowledge**
*Concepts ('know that')*
- Mechanical elements (lever, pulley, gear) change force or speed; increasing one decreases the other.
- A motor operating under load draws more current and may fail if the load exceeds its capacity.
- Microcontroller IO pins cannot directly drive motors due to current limitations.

*Substantive Knowledge ('know about')*
- Short circuits, high-current batteries (e.g., LiPo), and mechanical pinch points are primary safety hazards in motorised systems.
- A driver circuit acts as the high-current interface between a low-current microcontroller and an actuator.
- Mechanisms fail when poorly mounted; rigid support requires mechanical fasteners (screws, standoffs), not adhesives.

*Procedural Knowledge ('know how')*
- Safety mitigation requires identifying and securing electrical shorts and pinch points before power-on.
- Current draw must be measured to understand how a system behaves under varying load conditions.

**Practices**
*Tools and Skills ('know how to use')*
- Construct a rigid mechanical mount for a motor using specific fasteners (M3 screws, standoffs).
- Wire a motor through a dedicated driver circuit (e.g., L298N).
- Use a multimeter to record current draw under different load conditions.

*Application ('know how to apply')*
- Identify and mitigate safety hazards (electrical shorts, pinch points) before powering on a motorised system.
- Add a simple mechanical element (e.g., a gear or lever) and compare moving a load with and without it.
- Observe and document what happens when a mechanism is loaded versus unloaded, referencing current draw."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Describe a threshold decision.*?Identify one thing the system does badly and explain the cause",
        """**Knowledge**
*Concepts ('know that')*
- A threshold decision (if X, then do Y) is the fundamental control act in a sensor–actuator system.
- The complete system chain flows sequentially: sensor → measurement → decision → actuator → status.
- A system without status output is incomplete; operator feedback is a core design requirement.

*Substantive Knowledge ('know about')*
- Systems operate in meaningful states (e.g., Idle, Active, Error) with defined transitions between them.
- Fault injection is a deliberate engineering technique used to reveal how a system behaves when a component fails.

*Procedural Knowledge ('know how')*
- Status indication (e.g., LEDs, buzzers) is used to communicate the current system state to the operator.
- Disconnecting a sensor mid-operation is a standard method for testing fault response.

**Practices**
*Tools and Skills ('know how to use')*
- Implement a threshold decision in code that changes actuator behaviour based on a sensor reading.
- Add status indication (e.g., distinct LED patterns) for at least two system states.

*Application ('know how to apply')*
- Disconnect a sensor mid-run (fault injection); describe and record the system's response.
- Trace the system's behaviour in words, matching the observed physical actions to the code logic.
- Identify one specific weakness in the system's behaviour and explain its cause."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Explain how voltage dividers.*?Document digital sensor integration \(address, library, confirmed parameters\) as part of a build log",
        """**Knowledge**
*Concepts ('know that')*
- An Analogue-to-Digital Converter (ADC) converts a voltage to a digital count; resolution and quantisation limit measurement precision.
- The loading effect means connecting measurement equipment or a circuit to a sensor output can change that output.
- Most modern sensors communicate digitally; I2C is a protocol where addressed devices share a common bus.

*Substantive Knowledge ('know about')*
- Voltage dividers produce a varying voltage from a varying resistance (e.g., thermistor, LDR).
- Noise is a measurable property characterised by minimum, maximum, and range.
- Software filtering (e.g., moving average) introduces a fundamental trade-off between signal stability and response lag.
- Datasheets contain key parameters (operating range, output format, accuracy, I2C address) that dictate circuit decisions.

*Procedural Knowledge ('know how')*
- Calibration establishes the relationship between a sensor's electrical output and the physical quantity.
- Simulation is a pre-build modelling tool that will inevitably differ from physical reality.

**Practices**
*Tools and Skills ('know how to use')*
- Build and calibrate an analogue sensor chain, producing a measured calibration curve with at least five data points.
- Read a digital sensor via a library, identify its I2C address, and confirm communication via the serial monitor.
- Apply a moving average software filter to a noisy signal.

*Application ('know how to apply')*
- Capture a 200+ sample noise floor and use the calculated range to justify safe threshold placement.
- Log and display the stability-versus-lag trade-off of a software filter using measured data.
- Extract key parameters from a datasheet and apply them to a specific circuit or threshold decision.
- Place two I2C devices on the same bus and confirm both return valid readings."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Explain PWM duty cycle.*?Select a driver component from a datasheet for a given motor specification; document the selection reasoning",
        """**Knowledge**
*Concepts ('know that')*
- Pulse Width Modulation (PWM) duty cycle controls the average power delivered to a load by varying the percentage of on-time.
- Supply voltage droops under load; severe droop causes microcontroller brownout and reset.
- Power dissipation must remain within component ratings to prevent destruction.

*Substantive Knowledge ('know about')*
- Motor startup current and stall current significantly exceed the rated running current.
- An H-bridge circuit enables direction control by reversing the flow of current through the motor.
- Driver circuits provide the high-current interface that microcontroller IO pins cannot.

*Procedural Knowledge ('know how')*
- Measuring supply voltage under load is necessary to identify droop and brownout risks.
- Datasheets are used to select driver components that match or exceed motor stall current specifications.

**Practices**
*Tools and Skills ('know how to use')*
- Drive a motor via PWM with a correct driver stage at multiple duty cycles (e.g., 25%, 50%, 75%, 100%).
- Wire and demonstrate an H-bridge circuit for forward/reverse direction control.
- Measure supply voltage and current draw simultaneously under load.

*Application ('know how to apply')*
- Record speed and supply voltage at different PWM duty cycles to plot and explain droop behaviour.
- Identify and describe the stall condition by recording current draw when the motor is mechanically blocked.
- Select a driver component from a datasheet for a specific motor, documenting the rating comparison."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Explain methods for securely connecting.*?Document mechanical decisions and integration challenges as part of design reasoning, including photographs",
        """**Knowledge**
*Concepts ('know that')*
- A motor that operates successfully unloaded will behave differently and may fail under real mechanical load.
- Friction, backlash, and binding are real mechanical losses that must be managed, not assumed away.

*Substantive Knowledge ('know about')*
- Secure load connection requires specific mechanical methods (set screws, D-shafts, couplers), not adhesives.
- Limit switches provide physical end-of-travel detection to stop mechanisms safely.
- Rotary-to-linear motion conversion is achieved through specific mechanisms (winch, rack and pinion, lead screw).

*Procedural Knowledge ('know how')*
- Mechanical integration requires identifying and adjusting physical binding sources during the build process.
- Selecting a mechanical arrangement requires matching the mechanism type to the specific load and speed requirements.

**Practices**
*Tools and Skills ('know how to use')*
- Securely attach a load to a motor shaft using a mechanical coupler or set screw.
- Install and wire a limit switch to a microcontroller input.
- Build a specific rotary-to-linear mechanism (e.g., a winch or rack and pinion).

*Application ('know how to apply')*
- Write code to stop a motor immediately when a limit switch is pressed.
- Identify friction or binding sources in a built mechanism, adjust the build to reduce them, and document the before-and-after behaviour.
- Justify the selection of a mechanical arrangement for a stated load and speed requirement."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Explain hysteresis as a dead band.*?Add status indication \(LED pattern or buzzer\) for at least two system states",
        """**Knowledge**
*Concepts ('know that')*
- Timing is a system property: sensor sampling, actuator response, and software loops operate at different, interacting rates.
- AI can generate code syntax and structure, but the engineer must verify the logic against physical system behaviour.
- Data output and operator status are core design requirements; a silent system is incomplete.

*Substantive Knowledge ('know about')*
- Hysteresis (deadband) prevents output chatter when a sensor signal fluctuates near a threshold.
- The `delay()` function blocks concurrent behaviour; `millis()` enables non-blocking timing.
- Mechanical buttons bounce; raw readings require debounce logic to be reliable.
- CSV (Comma-Separated Values) is a structured format that enables data graphing and analysis.

*Procedural Knowledge ('know how')*
- Serial communication is a diagnostic output channel; baud rate must be fast enough to prevent loop slowdowns.
- The Serial Plotter is used to visualise sensor data and system response in real time.

**Practices**
*Tools and Skills ('know how to use')*
- Implement a threshold with hysteresis in code.
- Implement software debounce for a physical button.
- Format multiple sensor readings and system states into a single CSV string over Serial.
- Use the Serial Plotter to visualise a changing physical quantity.

*Application ('know how to apply')*
- Demonstrate and document the before/after chatter behaviour when hysteresis is applied to a threshold.
- Replace blocking `delay()` code with non-blocking `millis()` code (or physically verify AI-generated non-blocking code).
- Measure loop timing to identify bottlenecks caused by excessive `Serial.print()` statements or low baud rates.
- Export logged CSV data to a spreadsheet to create a calibration or noise graph as evidence."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Explain how bypass capacitors.*?Write sensor selection reasoning as part of a design rationale document linking datasheet parameters to logged physical data",
        """**Knowledge**
*Concepts ('know that')*
- Signal integrity is degraded by noise pickup, long wires, and inadequate grounding.
- Measurement has absolute limits: drift, sensor hysteresis, and aging affect data in ways that logged output cannot always reveal.
- Simulation models diverge from physical reality in both predictable and unpredictable ways.

*Substantive Knowledge ('know about')*
- Bypass capacitors absorb supply voltage spikes to maintain local signal integrity.
- Datasheet specifications are guarantees with stated conditions, not general approximations.
- Sensor selection requires balancing accuracy, range, response time, and interface type against specific deployment needs.

*Procedural Knowledge ('know how')*
- AI is used to extract datasheet parameters efficiently, but the engineer must independently justify those parameters using physical evidence.
- Sensor accuracy must be validated against a known, calibrated reference.

**Practices**
*Tools and Skills ('know how to use')*
- Use AI to extract and summarise key parameters from a complex component datasheet.
- Install bypass capacitors and shielded wiring to improve signal integrity.
- Validate a sensor's accuracy against a known physical reference.

*Application ('know how to apply')*
- Select and justify a sensor against measurable requirements, supporting the choice with physical logged data.
- Diagnose a signal integrity problem (e.g., noise from a long cable) and mitigate it, proving the fix with before/after logged data.
- Use logged data to characterise sensor behaviour across a range of real-world operating conditions.
- Write a sensor selection rationale that explicitly links AI-extracted datasheet parameters to logged physical evidence."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Explain that sensors fail.*?Document what happens when a specific component fails and how the code responds — as a verification matrix entry",
        """**Knowledge**
*Concepts ('know that')*
- Sensors fail and wires break; systems must be designed to respond safely rather than hang, crash, or act on invalid data.
- A safe state is the specific, designed condition a system must enter when a fault occurs.
- The system's response to failure is a verifiable property that must be tested.

*Substantive Knowledge ('know about')*
- Timeout logic and range checks allow code to determine whether a sensor reading is valid before acting on it.
- Fault injection is the deliberate introduction of failures (e.g., unplugging a sensor) to verify resilience.

*Procedural Knowledge ('know how')*
- Code must actively validate incoming data streams rather than assuming they are correct.
- Documenting fault responses in a verification matrix proves the system's resilience.

**Practices**
*Tools and Skills ('know how to use')*
- Write code that validates a sensor reading using range checks and timeout limits.
- Program a defined safe state that halts actuation when data is invalid.

*Application ('know how to apply')*
- Test system resilience using fault injection (e.g., unplugging a sensor mid-run) and verify it enters the safe state.
- Document the system's response to specific component failures as formal entries in a verification matrix."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Calculate estimated runtime.*?Write power requirements as measurable statements and include them in the verification matrix",
        """**Knowledge**
*Concepts ('know that')*
- Energy efficiency is a critical design constraint for battery-powered and remote monitoring systems.
- Worst-case load analysis (peak draw), not idle or average draw, is the correct basis for power budget verification.

*Substantive Knowledge ('know about')*
- Estimated runtime is calculated from current draw and battery capacity ($E = I \\times t$).
- Brownout is the collapse of supply voltage under peak load, causing microcontroller resets or state corruption.
- Brownout mitigation strategies include bulk capacitance, regulated supplies, load shedding, and safe state entry.

*Procedural Knowledge ('know how')*
- A power budget table is a formal document requiring idle, active, and peak current measurements.
- The gap between calculated runtime and measured runtime must be documented and explained.

**Practices**
*Tools and Skills ('know how to use')*
- Measure current draw at idle, active, and peak states to populate a power budget table.
- Calculate estimated battery runtime using measured current and battery capacity.
- Implement a brownout mitigation strategy (e.g., adding bulk capacitance).

*Application ('know how to apply')*
- Measure actual runtime under worst-case load and explain the gap between the prediction and the physical result.
- Deliberately trigger a brownout in a real system, implement a mitigation, and verify the improvement with logged voltage data.
- Justify energy efficiency choices with measured evidence and write power requirements as measurable statements in the verification matrix."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Compare DC motor.*?Include mechanical performance criteria in the verification matrix with defined pass/fail thresholds",
        """**Knowledge**
*Concepts ('know that')*
- Actuator selection requires balancing trade-offs: DC motor (speed, cost), servo (position, simplicity), stepper (precision, complexity).
- Load and torque requirements must be calculated or estimated from first principles before selecting an actuator.

*Substantive Knowledge ('know about')*
- Friction, backlash, and binding are measurable mechanical losses that must be quantified in verification.
- Integration constraints include wiring paths, mounting rigidity, cable strain, and thermal behaviour.
- Repeatability is a core verification criterion: a mechanism must return to the same position reliably across multiple cycles.

*Procedural Knowledge ('know how')*
- Mechanical performance criteria must be defined with specific pass/fail thresholds in the verification matrix.
- Actuator justification requires matching the motor's specifications to the calculated physical load.

**Practices**
*Tools and Skills ('know how to use')*
- Calculate or estimate load and torque requirements for a specific mechanical task.
- Build a position or lift system that meets a stated load specification.
- Measure mechanical losses (friction, backlash) in a built system.

*Application ('know how to apply')*
- Compare different actuator types against design criteria and justify the final selection with documented reasoning.
- Identify and resolve integration failures (e.g., binding, loose mounts, cable strain) using physical evidence.
- Verify mechanism repeatability across multiple cycles and record the performance in the verification matrix."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Explain the difference.*?Write response requirements as measurable criteria; verify with logged data as evidence",
        """**Knowledge**
*Concepts ('know that')*
- Closed-loop control uses feedback to correct errors, but can introduce instability if poorly tuned.
- Increasing gain in a proportional system improves response speed but increases the risk of overshoot and oscillation.
- PID control combines Proportional (current error), Integral (steady-state error), and Derivative (overshoot) corrections.

*Substantive Knowledge ('know about')*
- Response characteristics include rise time, overshoot, settling time, and steady-state error.
- Simple ON/OFF feedback requires a deadband (hysteresis) to prevent rapid switching near the setpoint.
- Watchdog and timeout logic detect when a system is stuck and force a deliberate response.

*Procedural Knowledge ('know how')*
- Logged data is required to visualise and tune response characteristics (overshoot, settling time).
- Response requirements must be written as measurable criteria (e.g., "settles within 2 seconds").

**Practices**
*Tools and Skills ('know how to use')*
- Implement simple ON/OFF feedback control with a deadband.
- Implement Proportional (P-only) control and adjust the gain.
- Implement watchdog or timeout logic in a control loop.

*Application ('know how to apply')*
- Log the response of a P-only controller over time; identify and explain overshoot or instability.
- Iterate on feedback behaviour using logged evidence, documenting the trade-off made at each tuning step.
- Verify watchdog/timeout behaviour using fault injection and logged evidence.
- Describe the feedback-controlled system in plain language based on observed logged data."""
    ),
    (
        r"\*\*Learning Outcomes\*\*\nStudents will:\n- Explain why structured state machines.*?Maintain a version/change log throughout the project with meaningful, dated entries",
        """**Knowledge**
*Concepts ('know that')*
- Structured state machines replace nested if/else logic to ensure system behaviour is predictable and testable.
- Boundary testing verifies behaviour at the edges of specified ranges, where systems most often fail.
- Iterative testing ensures that a fix meets a requirement without breaking other passing tests (regression).

*Substantive Knowledge ('know about')*
- States (e.g., Idle, Measuring, Actuating, Error) require explicit, testable transition conditions.
- A verification matrix links each requirement to a test method, evidence, pass/fail result, and verdict.
- Requirements must be written as measurable, testable statements, not descriptions or intentions.

*Procedural Knowledge ('know how')*
- AI can generate state machine boilerplate, but the engineer must draw the logic and physically verify every transition.
- A version and change log is a required engineering discipline to track what changed, why, and what was retested.

**Practices**
*Tools and Skills ('know how to use')*
- Draw a state diagram identifying all states, transitions, and the Error/safe state before coding.
- Use AI to generate state machine boilerplate code based on the drawn diagram.
- Maintain a version/change log with meaningful, dated entries.

*Application ('know how to apply')*
- Verify that the AI-generated implementation matches the drawn diagram by physically testing every transition.
- Write a 5–8 requirement verification pack covering core functional requirements.
- Conduct boundary tests and fault injection, record failures honestly, iterate the design, and retest."""
    )
]

for old_pattern, new_text in replacements:
    content, count = re.subn(old_pattern, new_text, content, flags=re.DOTALL)
    if count == 0:
        print(f"Failed to replace pattern: {old_pattern[:50]}...")

with open('curriculum_ideas_v4.md', 'w') as f:
    f.write(content)

print("Done updating curriculum_ideas_v4.md")
