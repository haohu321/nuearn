pragma solidity >=0.6.1 <0.9.0;

// SPDX-License-Identifier: MIT
contract NuVault {
    string companyName = "Nuearn";

    struct Account {
        string name;
        uint256 numTokens;
    }

    mapping(string => Account) public nameToAccount;

    function addAccount(string memory name, uint256 numTokens) public {
        Account memory account = Account(name, numTokens);
        nameToAccount[name] = account;
    }

    function getNumTokens(string memory accountName)
        public
        view
        returns (uint256)
    {
        return nameToAccount[accountName].numTokens;
    }

    function getVaultInfo() public view returns (string memory) {
        return companyName;
    }
}
