<html>
<head>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript" src="/assets/arbor-v0.92/lib/arbor.js"></script>
<script type="text/javascript" src="/assets/graphics.js"></script>
<script type="text/javascript" src="/assets/renderer.js"></script>

<script type="text/javascript">

  $(document).ready(function() {
    var sys = arbor.ParticleSystem(1000, 600, 0.8);
    sys.parameters({gravity: true});
    sys.renderer = Renderer("#viewport")
    %if swimlane:
      sys.addNode('root', {'color': '{{nodeColors['root']}}', 'shape': 'rect', 'label': 'Swimlanes', 'link': '/swimchart'})
      %for item in data:
	%if item['ItemType'] == 'swimlane':
          sys.addNode('{{item['Uuid']}}', {'color': '{{nodeColors[item['ItemType']]}}', 'shape': 'rect', 'label': '{{item['Name']}}', 'link': '/swimchart?swimlane={{item['Name']}}'})
	%else:
          sys.addNode('{{item['Uuid']}}', {'color': '{{nodeColors[item['ItemType']]}}', 'shape': 'rect', 'label': '{{item['Name']}}'})
        %end
        %if item['ParentUuids']:
          %for parent in item['ParentUuids']:
            sys.addEdge('{{parent}}', '{{item['Uuid']}}', {'color': 'grey', 'directed': 1})
          %end
        %else:
	  sys.addEdge('root', '{{item['Uuid']}}', {'color': 'grey', 'directed': 1})
        %end
      %end
    %else:
      sys.addNode('root', {'color': '{{nodeColors['root']}}', 'shape': 'rect', 'label': 'Swimlanes'})
      %for item in data:
        %if item['ParentUuids']:
	  %continue
	%end
	%if item['ItemType'] == 'swimlane':
          sys.addNode('{{item['Uuid']}}', {'color': '{{nodeColors[item['ItemType']]}}', 'shape': 'rect', 'label': '{{item['Name']}}', 'link': '/swimchart?swimlane={{item['Name']}}'})
	%else:
          sys.addNode('{{item['Uuid']}}', {'color': '{{nodeColors[item['ItemType']]}}', 'shape': 'rect', 'label': '{{item['Name']}}'})
        %end
        sys.addEdge('root', '{{item['Uuid']}}', {'color': 'grey', 'directed': 1})
      %end
    %end

  });
</script>
</head>

<body>
<h1>SwimChart</h1>

  <canvas id="viewport" width="900" height="700"></canvas>

</body>
</html>
