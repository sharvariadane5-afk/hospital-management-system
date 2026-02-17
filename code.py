<!DOCTYPE html>
<html>
<head>
    <title>Hospital Management System</title>
    <style>
        body {
            font-family: Arial;
            background-color: #f2f2f2;
            text-align: center;
        }
        h1 {
            background-color: #2c7be5;
            color: white;
            padding: 15px;
        }
        form {
            background: white;
            padding: 20px;
            width: 400px;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }
        input, select {
            width: 90%;
            padding: 8px;
            margin: 8px 0;
        }
        button {
            padding: 10px 20px;
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }
        table {
            margin: 20px auto;
            border-collapse: collapse;
            width: 80%;
            background: white;
        }
        table, th, td {
            border: 1px solid black;
            padding: 10px;
        }
        th {
            background-color: #2c7be5;
            color: white;
        }
    </style>
</head>
<body>

    <h1>Hospital Management System</h1>

    <form>
        <h2>Patient Registration</h2>
        
        <input type="text" placeholder="Patient Name" required><br>
        <input type="number" placeholder="Age" required><br>
        
        <select required>
            <option value="">Select Gender</option>
            <option>Male</option>
            <option>Female</option>
            <option>Other</option>
        </select><br>

        <input type="text" placeholder="Disease" required><br>
        <input type="date" required><br>

        <button type="submit">Register</button>
    </form>

    <h2>Patient Records</h2>

    <table>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Gender</th>
            <th>Disease</th>
            <th>Date</th>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>30</td>
            <td>Male</td>
            <td>Fever</td>
            <td>2026-02-17</td>
        </tr>
    </table>

</body>
</html>
