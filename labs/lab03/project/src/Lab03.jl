
module Lab03

export daisyworld_point

function daisyworld_point(l)
    black = max(0.0, 0.45 - 0.35 * (l - 0.95)^2)
    white = max(0.0, 0.40 - 0.35 * (l - 1.10)^2)
    temp = 15 + 35 * l - 18 * black + 15 * white
    return black, white, temp
end

end
