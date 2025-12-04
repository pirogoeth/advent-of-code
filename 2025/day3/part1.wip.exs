defmodule Day3 do
  def largest_joltages(current, rest) do
    IO.inspect(current, rest)
    [first, second] = current
    case rest do
      [next | rest] ->
        cond do
          next > first ->
            first = next
            largest_joltages([first, second], rest)
          next > second ->
            second = next
            largest_joltages([first, second], rest)
          true ->
            largest_joltages([first, second], rest)
        end
      [] ->
        [first, second]
    end
  end
end

[fname | _] = System.argv()
inputs = File.read!(fname)

outputs = Enum.map(String.split(inputs, "\n"), fn batteries ->
  joltages = for joltageStr <- String.codepoints(batteries), do: Integer.parse(joltageStr)
  IO.inspect(joltages)
  [first, second | rest] = joltages

  Enum.map(
    Day3.largest_joltages([first, second], rest),
    fn measurement ->
      {joltage, _} = measurement 
      joltage
    end
  )
end)
IO.puts(outputs)
