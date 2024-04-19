// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DataStorage {
    mapping(string => string[]) data;

    function addData(string memory key, string memory value) public {
        data[key].push(value);
    }

    function getData(string memory key) public view returns (string[] memory) {
        return data[key];
    }
}
