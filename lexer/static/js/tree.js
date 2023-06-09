function Node(value) {
    // Private Properties
    const radius = 32.5;
  
    // Properties
    this.value = value;
    this.x = null;
    this.y = null;
    this.right = null;
    this.left = null;
  
    this.isLeaf = () => this.right == null && this.left == null;
  
    this.drawEdge = function (context, x, y, left_way, resolve) {
      context.strokeStyle = "gray";
      context.beginPath();
      const x_y_ratio = Math.abs(this.y - y) / Math.abs(this.x - x);
      const w = radius * Math.sqrt(1 / (1 + Math.pow(x_y_ratio, 2)));
      const d = x_y_ratio * w;
      if (left_way) {
        drawEdgeAnimated(this.x - w, this.y + d, x + w, y - d, context, resolve);
      } else {
        drawEdgeAnimated(this.x + w, this.y + d, x - w, y - d, context, resolve);
      }
    };
  
    this.draw = function (context) {
      context.beginPath();
      context.arc(this.x, this.y, radius, 0, Math.PI * 2, false);
      context.fillStyle = "white";
      context.fill();
      context.strokeStyle = "#212121";
      context.stroke();
      context.font = "25px Times New Roman";
      context.textAlign = "center";
      context.textBaseline = "middle";
      context.fillStyle = "#212121";
  
      // Adjust the representation based on the value type
      if (typeof this.value === "string") {
        context.fillText(this.value, this.x, this.y);
      } else {
        const valueText = String(this.value);
        const maxTextLength = 4; // Maximum length of text to be displayed
        const abbreviatedText =
          valueText.length > maxTextLength
            ? valueText.substring(0, maxTextLength - 1) + "..."
            : valueText;
        context.fillText(abbreviatedText, this.x, this.y);
      }
    };
  }
  
  function drawEdgeAnimated(origin_x, origin_y, destine_x, destine_y, ctx, resolve) {
    const vertices = [
      { x: origin_x, y: origin_y },
      { x: destine_x, y: destine_y },
    ];
    const N = 35;
    var waypoints = [];
    for (var i = 1; i < vertices.length; i++) {
      var pt0 = vertices[i - 1];
      var pt1 = vertices[i];
      var dx = pt1.x - pt0.x;
      var dy = pt1.y - pt0.y;
      for (var j = 0; j <= N; j++) {
        var x = pt0.x + (dx * j) / N;
        var y = pt0.y + (dy * j) / N;
        waypoints.push({ x: x, y: y });
      }
    }
    var t = 1;
    function resolveCallback(callback) {
      function animate() {
        if (t < waypoints.length - 1) {
          requestAnimationFrame(animate);
        } else {
          callback();
        }
        ctx.beginPath();
        ctx.moveTo(waypoints[t - 1].x, waypoints[t - 1].y);
        ctx.lineTo(waypoints[t].x, waypoints[t].y);
        ctx.stroke();
        t++;
      }
      return animate;
    }
  
    requestAnimationFrame(resolveCallback(resolve));
  }
  
  function constructTree(postfix) {
    const OPERATORS = ["*", "/", "-", "+"];
    var stack = [];
    var root = null;
    var current;
    var shift = false;
  
    for (var i = postfix.length - 1; i >= 0; i--) {
      if (null === root) {
        if (OPERATORS.includes(postfix[i])) {
          current = new Node(postfix[i]);
        } else {
          current = new Node(parseFloat(postfix[i]));
        }
        root = current;
      } else {
        if (shift) {
          if (OPERATORS.includes(postfix[i])) {
            current.left = new Node(postfix[i]);
          } else {
            current.left = new Node(parseFloat(postfix[i]));
          }
          current = current.left;
          shift = false;
        } else {
          if (OPERATORS.includes(postfix[i])) {
            current.right = new Node(postfix[i]);
          } else {
            current.right = new Node(parseFloat(postfix[i]));
          }
          current = current.right;
        }
      }
      if (OPERATORS.includes(postfix[i])) {
        stack.push(current);
      } else {
        current = stack.pop();
        shift = true;
      }
    }
  
    return root;
  }
  