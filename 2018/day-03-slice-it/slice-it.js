function getOverlappingArea(input) {
  const lines = input.split('\n');

  const rectangles = lines.map(line => {
    splitLine = line.split('@');
    const id = splitLine[0].trim();
    const splitDimensions = splitLine[1].split(':');
    const coordinates = splitDimensions[0];
    const splitCoordinates = coordinates.split(',');
    const widthHeight = splitDimensions[1];
    const splitWidthHeight = widthHeight.split('x');

    return {
      id,
      coordinates: {
        x1: Number(splitCoordinates[0]),
        y1: Number(splitCoordinates[1]),
        x2: Number(splitCoordinates[0]) + Number(splitWidthHeight[0] - 1),
        y2: Number(splitCoordinates[1]) + Number(splitWidthHeight[1] - 1)
      }
    };
  });

  const gridDimension = rectangles.reduce(
    (dimensions, rectangle) => {
      if (rectangle.coordinates.x2 > dimensions.width) {
        dimensions.width = rectangle.coordinates.x2;
      }
      if (rectangle.coordinates.y2 > dimensions.height) {
        dimensions.height = rectangle.coordinates.y2;
      }

      return dimensions;
    },
    {width: 0, height: 0}
  );

  const grid = [...Array.from(Array(gridDimension.width), () => 0)].map(e =>
    Array.from(Array(gridDimension.height), () => 0)
  );

  const countGrid = grid.map((column, indexC) => {
    return column.map((row, indexR) => {
      return rectangles.reduce((count, rectangle) => {
        if (
          indexC >= rectangle.coordinates.x1 &&
          indexC <= rectangle.coordinates.x2 &&
          indexR >= rectangle.coordinates.y1 &&
          indexR <= rectangle.coordinates.y2
        ) {
          count = count + 1;
        }

        return count;
      }, 0);
    });
  });

  return countGrid.reduce((count, column) => {
    return count + column.filter(row => row > 1).length;
  }, 0);
}

function getNonOverlappingId(input) {
  const lines = input.split('\n');

  const rectangles = lines.map(line => {
    splitLine = line.split('@');
    const id = splitLine[0].trim();
    const splitDimensions = splitLine[1].split(':');
    const coordinates = splitDimensions[0];
    const splitCoordinates = coordinates.split(',');
    const widthHeight = splitDimensions[1];
    const splitWidthHeight = widthHeight.split('x');

    return {
      id,
      coordinates: {
        x1: Number(splitCoordinates[0]),
        y1: Number(splitCoordinates[1]),
        x2: Number(splitCoordinates[0]) + Number(splitWidthHeight[0] - 1),
        y2: Number(splitCoordinates[1]) + Number(splitWidthHeight[1] - 1)
      }
    };
  });

  let id = '';
  rectangles.forEach(rectangle => {
    const hasNoOverlap = rectangles
      .filter(rect => rectangle.id !== rect.id)
      .every(rect => {
        return (
          rectangle.coordinates.x1 > rect.coordinates.x2 ||
          rectangle.coordinates.x2 < rect.coordinates.x1 ||
          rectangle.coordinates.y1 > rect.coordinates.y2 ||
          rectangle.coordinates.y2 < rect.coordinates.y1
        );
      });

    if (hasNoOverlap) {
      id = rectangle.id;
    }
  });

  return id;
}

module.exports = {getOverlappingArea, getNonOverlappingId};
