function getSize(root) {
    if (root === null) return 0;
    else
      return (
        getSize(root.left) + 1 + getSize(root.right)
      );
  }
  
  function setCoordinates(root, height, width, margin_x, margin_y) {
    if (root === null) return;
    setCoordinates(
      root.left,
      height - margin_y,
      width / 2,
      margin_x / 2,
      margin_y
    );
    root.x = width;
    root.y = height;
    setCoordinates(
      root.right,
      height - margin_y,
      width + margin_x,
      margin_x / 2,
      margin_y
    );
  }
  
  function print_coords(root) {
    if (root === null) return;
    console.log(root.x + ", " + root.y);
    print_coords(root.left);
    print_coords(root.right);
  }
  
  function drawTree(root, canvasId) {
    const canvas = document.getElementById(canvasId);
    const context = canvas.getContext("2d");
  
    const canvasWidth = canvas.width;
    const canvasHeight = canvas.height;
  
    const marginX = canvasWidth / (getSize(root) + 1);
    const marginY = canvasHeight / (Math.floor(canvasHeight / 150) + 1);
  
    setCoordinates(root, canvasHeight, marginX, marginX, marginY);
  
    // Clear canvas
    context.clearRect(0, 0, canvasWidth, canvasHeight);
  
    // Draw edges
    function drawEdges(node) {
      if (node === null) return;
      if (node.left) {
        node.drawEdge(context, node.left.x, node.left.y, true, () =>
          drawEdges(node.left)
        );
      }
      if (node.right) {
        node.drawEdge(context, node.right.x, node.right.y, false, () =>
          drawEdges(node.right)
        );
      }
    }
    drawEdges(root);
  
    // Draw nodes
    function drawNodes(node) {
      if (node === null) return;
      node.draw(context);
      drawNodes(node.left);
      drawNodes(node.right);
    }
    drawNodes(root);
  }
  