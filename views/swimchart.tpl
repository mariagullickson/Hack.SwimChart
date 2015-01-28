<html>
<head>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript" src="/assets/arbor-v0.92/lib/arbor.js"></script>
<script type="text/javascript" src="/assets/graphics.js"></script>
<script type="text/javascript" src="/assets/renderer.js"></script>

<script type="text/javascript">

  $(document).ready(function() {
    var sys = arbor.ParticleSystem(1000, 600, 0.5);
    sys.parameters({gravity: true});
    sys.renderer = Renderer("#viewport")
    %for item in data:
      sys.addNode('{{item['Uuid']}}', {color: '{{nodeColors[item['ItemType']]}}', 'shape': 'dot', 'label': '{{item['Name']}}'})

      %if item['ParentUuids']:
        %for parent in item['ParentUuids']:
          sys.addEdge('{{parent}}', '{{item['Uuid']}}')
        %end
      %end
    %end

  });
</script>
</head>

<body>
<h1>SwimChart</h1>

  <canvas id="viewport" width="1200" height="1000"></canvas>

</body>
</html>