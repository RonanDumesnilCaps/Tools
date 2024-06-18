<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matrice de Devis</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js"></script>
</head>

<body class="bg-gray-100 p-4">
    <div class="max-w-5xl mx-auto bg-white p-6 rounded-lg shadow-md">
        <div class="mb-4">
            <label for="quoteNumber" class="block text-sm font-medium text-gray-700">Numéro de Devis</label>
            <input type="text" id="quoteNumber" name="quoteNumber" class="mt-1 p-2 block w-full border border-gray-300 rounded-md">
        </div>
        <div class="mb-4">
            <label for="quoteDate" class="block text-sm font-medium text-gray-700">Date de Devis</label>
            <input type="date" id="quoteDate" name="quoteDate" class="mt-1 p-2 block w-full border border-gray-300 rounded-md">
        </div>
        <div class="mb-4">
            <label for="clientName" class="block text-sm font-medium text-gray-700">Nom du Client</label>
            <input type="text" id="clientName" name="clientName" class="mt-1 p-2 block w-full border border-gray-300 rounded-md">
        </div>
        <div class="mb-4">
            <label for="clientContact" class="block text-sm font-medium text-gray-700">Contact du Client</label>
            <input type="text" id="clientContact" name="clientContact" class="mt-1 p-2 block w-full border border-gray-300 rounded-md">
        </div>

        <div class="mb-8">
            <h2 class="text-xl font-bold mb-4">Liste des Services</h2>
            <table class="w-full mb-4">
                <thead>
                    <tr class="bg-gray-200">
                        <th class="p-2 text-left">Descriptif</th>
                        <th class="p-2 text-left">Tarif</th>
                        <th class="p-2 text-left">Action</th>
                    </tr>
                </thead>
                <tbody id="servicesTable">
                    <!-- Example service row -->
                    <tr>
                        <td class="p-2"><input type="text" name="desc_service_1" class="w-full border rounded p-1" value="Post Producteur"></td>
                        <td class="p-2"><input type="number" name="tarif_service_1" class="w-full border rounded p-1" value="1250"></td>
                        <td class="p-2"><button type="button" onclick="addServiceToQuote('desc_service_1', 'tarif_service_1')" class="bg-blue-500 text-white px-4 py-2 rounded">Ajouter</button></td>
                    </tr>
                </tbody>
            </table>
            <button type="button" onclick="addServiceRow()" class="bg-green-500 text-white px-4 py-2 rounded">Ajouter un Service</button>
        </div>

        <form id="devisForm">
            <table class="w-full mb-6">
                <thead>
                    <tr class="bg-gray-200">
                        <th class="p-2 text-left">DESCRIPTIF</th>
                        <th class="p-2 text-left">NB</th>
                        <th class="p-2 text-left">U</th>
                        <th class="p-2 text-left">NB/U</th>
                        <th class="p-2 text-left">TARIF</th>
                        <th class="p-2 text-left">REMISE</th>
                        <th class="p-2 text-left">TOTAL HT</th>
                        <th class="p-2 text-left">Action</th>
                    </tr>
                </thead>
                <tbody id="itemsTable">
                    <!-- Initial item rows will be added here dynamically -->
                </tbody>
            </table>

            <div class="mt-4">
                <p>Sous Total: <span id="subtotal">0.00 €</span></p>
                <p>TVA (20%): <span id="tva">0.00 €</span></p>
                <p>Total TTC: <span id="totalTTC">0.00 €</span></p>
            </div>

            <div class="mt-4">
                <button type="button" onclick="calculateTotal()" class="bg-blue-500 text-white px-4 py-2 rounded">Calculer le total</button>
            </div>

            <div class="mt-4">
                <button type="button" onclick="exportPDF()" class="bg-purple-500 text-white px-4 py-2 rounded">Exporter en PDF</button>
            </div>
        </form>
    </div>

    <script>
        let serviceCount = 1;

        function addServiceRow() {
            serviceCount++;
            const servicesTable = document.getElementById('servicesTable');
            const newRow = document.createElement('tr');
            newRow.innerHTML = `
                <td class="p-2"><input type="text" name="desc_service_${serviceCount}" class="w-full border rounded p-1"></td>
                <td class="p-2"><input type="number" name="tarif_service_${serviceCount}" class="w-full border rounded p-1"></td>
                <td class="p-2"><button type="button" onclick="addServiceToQuote('desc_service_${serviceCount}', 'tarif_service_${serviceCount}')" class="bg-blue-500 text-white px-4 py-2 rounded">Ajouter</button></td>
            `;
            servicesTable.appendChild(newRow);
        }

        function addServiceToQuote(descId, tarifId) {
            const desc = document.getElementsByName(descId)[0].value;
            const tarif = document.getElementsByName(tarifId)[0].value;
            const itemsTable = document.getElementById('itemsTable');
            const newRow = document.createElement('tr');
            newRow.innerHTML = `
                <td class="p-2"><input type="text" name="desc_${descId}" class="w-full border rounded p-1" value="${desc}" readonly></td>
                <td class="p-2"><input type="number" name="nb_${descId}" class="w-full border rounded p-1" value="1"></td>
                <td class="p-2">U</td>
                <td class="p-2"><input type="number" name="nbu_${descId}" class="w-full border rounded p-1" value="1"></td>
                <td class="p-2"><input type="number" name="tarif_${descId}" class="w-full border rounded p-1" value="${tarif}" readonly></td>
                <td class="p-2"><input type="number" name="remise_${descId}" class="w-full border rounded p-1" value="0"></td>
                <td class="p-2"><input type="text" name="totalht_${descId}" class="w-full border rounded p-1" readonly></td>
                <td class="p-2"><button type="button" onclick="removeRow(this)" class="bg-red-500 text-white px-2 py-1 rounded">X</button></td>
            `;
            itemsTable.appendChild(newRow);
        }

        function calculateTotal() {
            const form = document.forms['devisForm'];
            const itemsTable = document.getElementById('itemsTable');
            const rows = itemsTable.querySelectorAll('tr');
            let subtotal = 0;

            rows.forEach(row => {
                const nb = parseFloat(row.querySelector('input[name^="nb_"]').value);
                const nbu = parseFloat(row.querySelector('input[name^="nbu_"]').value);
                const tarif = parseFloat(row.querySelector('input[name^="tarif_"]').value