var packageList = document.getElementById('package-list');
packages.map(function (pkg) {
    var packageItem = document.createElement('li');
    var packageLink = document.createElement('a');
    var packageName = document.createTextNode(pkg);
    packageLink.appendChild(packageName);
    packageLink.href = pkg;
    packageLink.download = pkg;
    packageItem.appendChild(packageLink);
    packageList.appendChild(packageItem);
})