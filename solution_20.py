def push(modules):
    low_pulses, high_pulses = 0, 0
    pulse_queue = [('broadcaster', False, None)]
    low_pulsed = set()
    while len(pulse_queue) > 0:
        pulse = pulse_queue.pop(0)
        pulse_high = pulse[1]
        module_name = pulse[0]
        if pulse[1]:
            high_pulses += 1
        else:
            low_pulses += 1
            low_pulsed.add(module_name)
        if module_name not in modules:
            continue
        module = modules[module_name]
        if module[0] == 'b':
            for next_module in module[1]:
                pulse_queue.append((next_module, False, module_name))
        elif module[0] == '%' and not pulse_high:
            module[2] = not module[2]
            for next_module in module[1]:
                pulse_queue.append((next_module, module[2], module_name))
        elif module[0] == '&':
            module[3][pulse[2]] = pulse_high
            all_true = False not in module[3].values()
            for next_module in module[1]:
                pulse_queue.append((next_module, not all_true, module_name))
    return (low_pulses, high_pulses, low_pulsed)

def parse_modules(puzzle_input):
    modules = {y.split(" -> ")[0].replace('%','').replace('&',''):[y.split(" -> ")[0][0], y.split(" -> ")[1].split(", "), False, {}] for y in puzzle_input.strip().splitlines()}
    for module_name in modules.keys():
        module = modules[module_name]
        for target_module in module[1]:
            if target_module in modules and modules[target_module][0] == '&':
                modules[target_module][3][module_name] = False
    return modules

def solve(puzzle_input):
    modules = parse_modules(puzzle_input)
    low_pulses, high_pulses = 0, 0
    for i in range(0, 1000):
        pulses = push(modules)
        low_pulses += pulses[0]
        high_pulses += pulses[1]
    print(low_pulses * high_pulses)

    modules = parse_modules(puzzle_input)
    count = 0
    module_pulse_intervals = {key:[] for key in modules.keys()}
    while not all([len(x) == 1 for x in module_pulse_intervals.values()]):
        count += 1
        pulses = push(modules)
        for low_pulsed in pulses[2]:
            if len(module_pulse_intervals[low_pulsed]) < 1:
                module_pulse_intervals[low_pulsed].append(count)
    
    for module in modules.values():
        if 'rx' in module[1]:
            dependencies = module[3].keys()
            intervals = sorted([module_pulse_intervals[x][0] for x in dependencies], reverse=True)
            common_interval = intervals[0]
            for interval in intervals[1:]:
                if common_interval % interval != 0:
                    common_interval *= interval
    print(common_interval)

    return

solve('''
%cg -> mt, hb
%sp -> xm
%nr -> hf, mt
broadcaster -> tl, gd, zb, gc
&qz -> qn
%df -> hd
%vg -> rm, kx
%gm -> mt, md
%ls -> hc
%lq -> zq, fx
&zd -> bz, kg, zb, lf, sq, zk, jx
%lz -> mt
%sq -> zk
%zn -> kx, tc
&zq -> mb, hc, qz, ql, tl, ls
&mt -> zm, tt, mh, gd, md
%lm -> mb, zq
%hf -> mt, sm
%hb -> mh, mt
%rm -> kx
%gc -> kx, sp
&cq -> qn
%mh -> jt
%zm -> nr
%xm -> kx, ld
&jx -> qn
&qn -> rx
%mp -> qt, kx
%zk -> vj
%hd -> mp, kx
%tl -> zq, hl
%zb -> zd, ph
%cl -> zd
&tt -> qn
%ld -> zn
%js -> lq, zq
%sm -> mt, lz
%qt -> vg, kx
%md -> cg
%vj -> bz, zd
%qs -> zd, fs
%mb -> ps
&kx -> cq, gc, sp, df, ld
%hc -> lm
%tc -> df, kx
%ps -> js, zq
%fs -> qc, zd
%hl -> jj, zq
%bz -> qs
%jj -> zq, ql
%ql -> ls
%ph -> kg, zd
%qc -> cl, zd
%lf -> sq
%kg -> lf
%fx -> zq
%jt -> zm, mt
%gd -> gm, mt
''')