
include(joinpath(@__DIR__, "..", "src", "Lab03.jl"))
using .Lab03

black, white, temp = daisyworld_point(1.0)
println(round(black; digits=3), " ", round(white; digits=3), " ", round(temp; digits=3))
