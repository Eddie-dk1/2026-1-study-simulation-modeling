
module Lab05

export next_state

function next_state(thinking::Int, eating::Int)
    return max(thinking - 1, 0), eating + 1
end

end
