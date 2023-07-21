model controller
  input Real ti;
  input Real weight;
  parameter Real weight_max;
  parameter Real tl;
  output Real w;
  output Boolean engine_on;
equation
  if (ti < tl) then
    engine_on = false;
  else
    engine_on = true;
  end if;

  if (weight < weight_max and engine_on == false) then
    w = 1.;
  else
    w = 0.;
  end if;

end controller;
