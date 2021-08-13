--A Script to insert a marker 4 seconds before the play
--or record head.
-- February 18, 2021
-- Able Kirby


-- Compute marker location delayed behind play-head
-- Avoid negitive times by linearly scaling delay near 0
pp = reaper.GetPlayPosition()
dly = 4
if (pp < 2*dly)
then
  pp = pp/2;
else
  pp = pp-dly 
end
  
-- Add Marker at positiong
reaper.AddProjectMarker2(0, 0, pp, 0, "++", -1, 0)
  
