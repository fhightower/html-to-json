# Interactive Demo

The two demos below run the real `html-to-json` library directly in your browser using [Pyodide](https://pyodide.org/) — no server, no install. Edit the HTML, flip the options, and watch the JSON update.

## 1. `convert()` — any HTML → JSON

<div class="h2j-demo" markdown="0">
    <div class="h2j-row">
        <strong>Load example:</strong>
        <select onchange="loadExample('convertInput', this.value); this.selectedIndex=0;">
            <option value="">Choose…</option>
            <option value="head_meta">README: head/meta block</option>
            <option value="simple">Simple article snippet</option>
        </select>
        <span id="convertStatus" class="h2j-status">Booting…</span>
    </div>
    <textarea id="convertInput" spellcheck="false"><head>
    <title>Floyd Hightower's Projects</title>
    <meta charset="UTF-8">
    <meta name="description" content="Floyd Hightower's Projects">
    <meta name="keywords" content="projects,fhightower,Floyd,Hightower">
</head></textarea>
    <div class="h2j-options">
        <label><input type="checkbox" id="captureValues" checked> capture_element_values</label>
        <label><input type="checkbox" id="captureAttributes" checked> capture_element_attributes</label>
    </div>
    <div class="h2j-row">
        <button class="md-button md-button--primary" id="convertRunBtn" onclick="runConvert()" disabled>Convert</button>
    </div>
    <div class="h2j-output-actions">
        <button class="md-button" onclick="copyOutput('convertOutput', this)">Copy JSON</button>
        <button class="md-button" onclick="downloadOutput('convertOutput', 'converted.json')">Download JSON</button>
    </div>
    <pre id="convertOutput"></pre>
</div>

## 2. `convert_tables()` — HTML tables → JSON

<div class="h2j-demo" markdown="0">
    <div class="h2j-row">
        <strong>Load example:</strong>
        <select onchange="loadExample('tablesInput', this.value); this.selectedIndex=0;">
            <option value="">Choose…</option>
            <option value="table_headers_row">README: malware table (headers in first row)</option>
            <option value="table_no_headers">Table without headers</option>
        </select>
        <span id="tablesStatus" class="h2j-status">Booting…</span>
    </div>
    <textarea id="tablesInput" spellcheck="false"><table>
    <tr>
        <th>#</th>
        <th>Malware</th>
        <th>MD5</th>
        <th>Date Added</th>
    </tr>
    <tr>
        <td>25548</td>
        <td><a href="/stats/DarkComet/">DarkComet</a></td>
        <td><a href="/config/034a37b2a2307f876adc9538986d7b86">034a37b2a2307f876adc9538986d7b86</a></td>
        <td>July 9, 2018, 6:25 a.m.</td>
    </tr>
    <tr>
        <td>25547</td>
        <td><a href="/stats/DarkComet/">DarkComet</a></td>
        <td><a href="/config/706eeefbac3de4d58b27d964173999c3">706eeefbac3de4d58b27d964173999c3</a></td>
        <td>July 7, 2018, 6:25 a.m.</td>
    </tr>
</table></textarea>
    <div class="h2j-options">
        <label><input type="checkbox" id="recordHtml"> record_html</label>
        <label><input type="checkbox" id="recordChildren"> record_children</label>
    </div>
    <div class="h2j-row">
        <button class="md-button md-button--primary" id="tablesRunBtn" onclick="runTables()" disabled>Convert tables</button>
    </div>
    <div class="h2j-output-actions">
        <button class="md-button" onclick="copyOutput('tablesOutput', this)">Copy JSON</button>
        <button class="md-button" onclick="downloadOutput('tablesOutput', 'tables.json')">Download JSON</button>
    </div>
    <pre id="tablesOutput"></pre>
</div>

!!! info "About this demo"
    The widgets above run Python in the browser via [Pyodide](https://pyodide.org/) and [WebAssembly](https://webassembly.org/). The first load installs the `html-to-json` wheel from PyPI in-browser and takes a few seconds; subsequent conversions are instant.
