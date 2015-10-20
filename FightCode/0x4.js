
//FightCode can only understand your robot
//if its class is called Robot

var tx = 0;
var ty = 0;
var count = 0;

var Robot = function(robot) {
  robot.clone();
};

Robot.prototype.onIdle = function(ev) {
  var robot = ev.robot;
  var x = robot.position.x;
  var y = robot.position.y;
  var point = 0;
  if (x < tx){
    if (y < ty){
      point = Math.atan((ty-y)/(tx-x)) * 180/Math.PI;
      point += 180;
    }
    else if (y > ty){
      point = Math.atan((tx-x)/(y-ty)) * 180/Math.PI;
      point += 90;
    }
    else{
      point = 180;
    }
  }
  else if (x > tx){
    if (y < ty){
      point = Math.atan((x-tx)/(ty-y)) * 180/Math.PI;
      point += 270;
    }
    else if (y > ty){
      point = Math.atan((y-ty)/(x-tx)) * 180/Math.PI;
      point += 0;
    }
    else{
      point = 0;
    }
  }
  else{
    if (y < ty){
      point = 90;
    }
    else{
      point = 270;
    }
  }
  var angle = robot.cannonAbsoluteAngle;
  var adj = Math.round(point-angle);
  if (count == 100){
    adj = 360;
    count = 0;
  }
  robot.rotateCannon(adj);
  robot.log(point, angle, adj, tx, ty, x, y);
  count += 1;
  robot.ahead(20);
  //robot.stop();
};

Robot.prototype.onWallCollision = function(ev) {
    var robot = ev.robot;
    robot.turn(ev.bearing + 90); // turn enought to be in a straight
                            // angle with the wall.
};

Robot.prototype.onRobotCollision = function(ev) {
    var robot = ev.robot;
    robot.turn(90);
};

Robot.prototype.onScannedRobot = function(ev) {
  var robot = ev.robot, scannedRobot = ev.scannedRobot;
  if (robot.id == scannedRobot.parentId || robot.parentId == scannedRobot.id) {
      return;
  }
  robot.fire();
	tx = ev.scannedRobot.position.x;
  ty = ev.scannedRobot.position.y;
  count = 0;
};
