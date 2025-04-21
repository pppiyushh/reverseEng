import angr
import claripy

proj = angr.Project("Zero Symbols")
password = claripy.BVS("password", 64 * 8)
cstate = proj.factory.call_state(
    proj.loader.main_object.mapped_base + 0x1169, # offset within file of pwd hashing function
    angr.PointerWrapper(claripy.Concat(password, claripy.BVV(0, 8)), buffer=True),
    cc=proj.factory.cc(),
)

for i in range(password.length // 8):
    b = password.get_byte(i)
    cstate.solver.add(
            claripy.Or(
                claripy.And(b >= ord("!"), b <= ord("~")),
                b == 0x00,
            )
    )


simgr = proj.factory.simulation_manager(cstate)
simgr.run()

for state in simgr.deadended:
    try:
        state.solver.add(state.regs.rax == 0x9E52FCA7)
        password = state.solver.eval(password).to_bytes(64).split(b"\x00", 1)[0].decode()
        print(f"The password is {password!r}")
        break
    except Exception as e:
        print("Exc", e)
